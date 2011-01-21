from dateutil.relativedelta import *

def get_next_paypal_monthly_billing_date(curr_date):
    '''
    Calculate a PayPal Subscription Renewal Date
    
    For monthly billing cycles, recurring payments are collected on the same 
    day of the month. If the initial recurring payment falls on the 31st, 
    PayPal eventually adjusts the billing cycle to the 1st of the month. If
    the initial recurring payment falls on the 29th or 30th, PayPal adjusts
    the billing cycle to the 1st of March following that skipped February. 
    '''
    
    new_date = curr_date + relativedelta(months=+1)
    if new_date.day < curr_date.day:
        new_date = new_date + relativedelta(days=+1)
        
    return new_date

    