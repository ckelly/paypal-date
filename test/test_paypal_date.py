import unittest
import datetime

from paypal_date import get_next_paypal_monthly_billing_date

class TestPayPalDate(unittest.TestCase):

    def setUp(self):
        pass

    def test_default(self):
        # default test case - all months have same day of month
        start_date = datetime.datetime(2009, 4, 15)
        
        expected_result = [
            datetime.datetime(2009, 5, 15),
            datetime.datetime(2009, 6, 15),
            datetime.datetime(2009, 7, 15),
            datetime.datetime(2009, 8, 15),
            datetime.datetime(2009, 9, 15),
            datetime.datetime(2009, 10, 15),
            datetime.datetime(2009, 11, 15),
            datetime.datetime(2009, 12, 15),
            datetime.datetime(2010, 1, 15),
            datetime.datetime(2010, 2, 15)
        ]
        
        for i in xrange(0, 10):
            start_date = get_next_paypal_monthly_billing_date(start_date)
            self.assertEqual(start_date, expected_result[i])

    def test_month_end_1(self):
        # monthly edge case 1 - 31st
        start_date = datetime.datetime(2009, 8, 31)

        expected_result = [
            datetime.datetime(2009, 10, 1),
            datetime.datetime(2009, 11, 1),
            datetime.datetime(2009, 12, 1),
            datetime.datetime(2010, 1, 1),
            datetime.datetime(2010, 2, 1),
            datetime.datetime(2010, 3, 1),
            datetime.datetime(2010, 4, 1),
            datetime.datetime(2010, 5, 1),
            datetime.datetime(2010, 6, 1)
        ]
        
        for i in xrange(0, 9):
            start_date = get_next_paypal_monthly_billing_date(start_date)
            self.assertEqual(start_date, expected_result[i])

    def test_month_end_2(self):
        # monthly edge case 2 - 30th
        start_date = datetime.datetime(2009, 12, 30)

        expected_result = [
            datetime.datetime(2010, 1, 30),
            datetime.datetime(2010, 3, 1),
            datetime.datetime(2010, 4, 1),
            datetime.datetime(2010, 5, 1),
            datetime.datetime(2010, 6, 1),
            datetime.datetime(2010, 7, 1),
            datetime.datetime(2010, 8, 1),
            datetime.datetime(2010, 9, 1),
            datetime.datetime(2010, 10, 1),
            datetime.datetime(2010, 11, 1)
        ]
        
        for i in xrange(0, 10):
            start_date = get_next_paypal_monthly_billing_date(start_date)
            self.assertEqual(start_date, expected_result[i])

    def test_leap_year(self):
        # leap year test case
        start_date = datetime.datetime(2008, 1, 29)

        expected_result = [
            datetime.datetime(2008, 2, 29),
            datetime.datetime(2008, 3, 29),
            datetime.datetime(2008, 4, 29),
            datetime.datetime(2008, 5, 29),
            datetime.datetime(2008, 6, 29),
            datetime.datetime(2008, 7, 29),
            datetime.datetime(2008, 8, 29),
            datetime.datetime(2008, 9, 29),
            datetime.datetime(2008, 10, 29),
            datetime.datetime(2008, 11, 29),
            datetime.datetime(2008, 12, 29),
            datetime.datetime(2009, 1, 29),
            datetime.datetime(2009, 3, 1),
            datetime.datetime(2009, 4, 1)
        ]
        
        for i in xrange(0, 14):
            start_date = get_next_paypal_monthly_billing_date(start_date)
            self.assertEqual(start_date, expected_result[i])

    def test_paypal_example_1(self):
        # leap year test case
        start_date = datetime.datetime(2010, 7, 31)

        expected_result = [
            datetime.datetime(2010, 8, 31),
            datetime.datetime(2010, 10, 1),
            datetime.datetime(2010, 11, 1),
        ]
        
        for i in xrange(0, 3):
            start_date = get_next_paypal_monthly_billing_date(start_date)
            self.assertEqual(start_date, expected_result[i])
            
    def test_paypal_example_2(self):
        # example from documentation
        start_date = datetime.datetime(2010, 12, 30)

        expected_result = [
            datetime.datetime(2011, 1, 30),
            datetime.datetime(2011, 3, 1),
            datetime.datetime(2011, 4, 1),
        ]
        
        for i in xrange(0, 3):
            start_date = get_next_paypal_monthly_billing_date(start_date)
            self.assertEqual(start_date, expected_result[i])

if __name__ == '__main__':
    unittest.main()