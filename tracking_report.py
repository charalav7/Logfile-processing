from itertools import islice
import os
import time
import numpy as np
import sys

date_pattern = '%Y-%m-%d %H:%M:%S%Z'

def startExec():
    in_path, logfile = get_log() # call get_log() to obtain the path of the logfile and the logfile itself
    start_date = get_start_date() # get start date
    end_date = get_end_date(start_date) #get end date
    report = process_log(logfile, start_date, end_date)  # call process_log function that returns a report array
    gen_report(report, in_path)  # finnaly generate the report in a specific file at the directory of the given log path


def get_log():
    in_path = input("\nWrite the path of the log file => ")
    logfile = check_log(in_path)
    if logfile:
        return in_path, logfile
    else:
        return get_log()


def check_log(in_path):
    # check file extension of the given path, accept only .log and .txt files
    if in_path.lower().endswith(('.log', '.txt')):
        # check if the path is actually correct
        try:
            log_file = open(in_path, 'r')
            return log_file
        except IOError:
            print("Wrong path! Try again!")
            return False
    else:
        print('Wrong path! Try again!')
        return False


def get_start_date():
    start_date = input('Give start date, e.g. 2013-09-01 09:00:00UTC => ')
    int_start_date = check_date(start_date)
    if int_start_date:
        #print('Printed inside', int_start_date)
        return int_start_date
    else:
        return get_start_date()


def get_end_date(int_start_date):
    end_date = input('Give end date, e.g. 2013-09-01 11:00:00UTC => ')
    int_end_date = check_date(end_date)
    if int_end_date:
        if check_date_greater(int_start_date, int_end_date):
            return (int_end_date)
        else:
            print("End date must be greater than start date! Try again!")
            return get_end_date(int_start_date)
    else:
        return get_end_date(int_start_date)


def check_date(d):
    try:
        #convert date to int according to specific pattern
        ch_date = int(time.mktime(time.strptime(d, date_pattern)))
        return ch_date
    except:
        print("Wrong date pattern! Try again!")
        return False


def check_date_greater(int_start_date, int_end_date):
    if int_end_date >= int_start_date:
        return True
    else:
        return False


def process_log(logfile, start_date, end_date):
    date_range = False   #a value to be changed if the date range is inside the log file dates
    #iterate for every line in the logfile
    for line in islice(logfile, 1, None):
        #convert given date to epoch timestamp
        cur_date = int(time.mktime(time.strptime(line.split('|')[1], date_pattern + " ")))
        #defining the proper date range for our log search
        if end_date >= cur_date:
            if cur_date >= start_date:
                date_range = True
                url = line.split('|')[2]
                userid = line.split('|')[3]
                if 'report' not in locals():
                    #initialization of report array
                    report = np.array([[url, 1, {str(userid)}]])
                else:
                    #case that the url of the corresponding line is not already included in the report array
                    if not np.any(np.in1d(report, url)):
                        report = np.append(report, np.array([[url, 1, {str(userid)}]]), axis=0)
                    else:
                        url_index = np.where(url==report)[0][0]  #define the index of url occurance in the report array
                        report[url_index][1] +=1   #increase by one the counter of page views
                        #check if userid is not in the url's userid set
                        if userid not in report[url_index][2]:
                            #add userid to the url's set, thus indicating new visitor
                            report[url_index][2].add(userid)
    logfile.close()
    #in case the date range is not included in the log file we simply exit the execution
    if date_range == False:
        print("Date range not included in the log file!")
        sys.exit(0)

    return report


def gen_report(report, in_path):
    dir_path = os.path.abspath(os.path.dirname(in_path))  #defining the path directory to save there the generated report
    gen_rep = open(os.path.join(dir_path, 'gen_report_' + str(time.strftime('%Y%m%d%H%M%S')) + '.log'), 'w')  #create a new unique log file with a timestamp
    #writing all the required information to the new log file
    gen_rep.write('|{0:<20}|{1:<10}|{2:<8}|'.format("url", "page views", "visitors"))
    for elem in report:
        gen_rep.write('\n|{0:<20}|{1:<10}|{2:<8}|'.format(elem[0], elem[1], len(elem[2])))

    print("Processed report generated successfully in =>", dir_path)
    gen_rep.close()
    return True

if __name__ == '__main__':
    startExec()