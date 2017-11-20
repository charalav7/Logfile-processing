import unittest
import tracking_report

class TestTrackingReport(unittest.TestCase):

    def test_getWrongPath(self):
        self.assertEqual(tracking_report.check_log('asasd'), False)

    def test_checkDateType(self):
        self.assertIs(type(tracking_report.check_date('2013-09-01 09:00:00UTC')), int)

    def test_checkDate(self):
        self.assertEqual(tracking_report.check_date('2013-09-01 09:00:00UTC'), 1378022400)
        self.assertGreaterEqual(tracking_report.check_date('2013-09-01 12:00:00UTC'), tracking_report.check_date('2013-09-01 09:00:00UTC'))

    def test_checkWrongDate(self):
        self.assertEqual(tracking_report.check_date('2013UTC'), False)

    def test_checkDateGreater(self):
        self.assertEqual(tracking_report.check_date_greater('2013-09-01 10:00:00UTC', '2013-09-01 12:00:00UTC'), True)
        self.assertEqual(tracking_report.check_date_greater('2013-09-01 09:00:00UTC', '2013-09-01 08:00:00UTC'), False)

    def test_processLog(self):
        log_file = open('logfile.log', 'r')
        report = tracking_report.process_log(log_file, tracking_report.check_date('2013-09-01 09:00:00UTC'), tracking_report.check_date('2013-09-01 12:00:00UTC'))
        self.assertEqual(report[0][1], 5)
        self.assertEqual(len(report[0][2]), 4)
        self.assertEqual(report[1][1], 3)
        self.assertEqual(len(report[1][2]), 2)

    def test_exitProcessLog(self): #exit process log when the date range is not included in the logfile
        log_file = open('logfile.log', 'r')
        self.assertRaises(SystemExit, tracking_report.process_log, log_file, tracking_report.check_date('2014-09-01 09:00:00UTC'), tracking_report.check_date('2014-09-01 10:00:00UTC'))

    def test_genReport(self):
        log_file = open('logfile.log', 'r')
        report = tracking_report.process_log(log_file, tracking_report.check_date('2013-09-01 09:00:00UTC'), tracking_report.check_date('2013-09-01 12:00:00UTC'))
        self.assertEqual(tracking_report.gen_report(report, 'logfile.log'), True)


if __name__ == '__main__':
    unittest.main()