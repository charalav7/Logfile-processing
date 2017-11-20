# tracking report 


-----------------------
Running the program
-----------------------

- The implementation of the tracking report was made in Python.
- To run the program, simply open the 'tracking_report.py' file in whichever Python IDE and then run it by pressing the corresponding button.
- The program immediately asks for the path of the log file. In case the log file is located at the same folder with the .py file then 
  we simply type directly the name of the log file, e.g. logfile.log. Otherwise, in case of a Windows pc, the path can be, 
  e.g. C:\Users\chara\Box Sync\Funnel\logfile.log  
- After the successful declaration of the log file path, the program continues by asking the start date of our search in the log file. This
  must be in the following format: 2013-09-01 11:00:00UTC . Otherwise, the program can continue and repeat asking for the date.
- After the successful declaration of the start date, the program continues by asking the end date of the search. The same check procedure
  exists here, with addition of the fact that the end date must be greater than the start date.
- If everything worked fine, and the date range is between the dates of the log file, the program generates a new log report file at the 
  same folder where the initial log file is located. The name of the report log is 'gen_report_' followed by the exact date of creation.
- It was assumed that the format of the initial log file is the one of the 'logfile.log' file that is included in the zip. 
  It is really important to keep this format in order for the program to work as intended.   
  
  
-----------------------
Testing
-----------------------

- The program was tested with 8 seperate unit tests, which were successfully passed. 
- Before running the test file, it is very important to include 'tracking_report.py', 'test_tracking.py', 'logfile.log' files at the same folder.
- To run the test module, just open the 'test_tracking.py' file in a Python IDE and press the corresponding run button. 