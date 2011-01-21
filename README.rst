paypal-date
-----------

Calculate a PayPal Subscription Renewal Date

For monthly billing cycles, recurring payments are collected on the same day of the month. If the initial recurring payment falls on the 31st, PayPal eventually adjusts the billing cycle to the 1st of the month. If the initial recurring payment falls on the 29th or 30th, PayPal adjusts the billing cycle to the cycle to the 1st of March following that skipped February. 

This is useful for displaying a "renewal date"  on a user dashboard for monthly-renewed PayPal subscriptions.

From the PayPal Documentation: https://www.x.com/thread/48147

  **How Subscriptions with Monthly Billing Cycles Work**
  
  For monthly billing cycles, recurring payments are collected on the same day of the month. If the initial recurring payment falls on the 31st, PayPal eventually adjusts the billing cycle to the 1st of the month. If the initial recurring payment falls on the 29th or 30th, PayPal adjusts the billing cycle to the 1st of the month on the following February.
 
  When Monthly Recurring Payments Are Due and Collected on the 31st
  The subscription terms are:
 
  $25.99 USD a month; the subscriber signs up on Thursday, July 31.
 
  The subscriber is billed as follows:
 
    Thursday, July 31 = $25.99 USD
    Saturday, August 31 = $25.99 USD
    Wednesday, October 1= $25.99 USD
    Saturday, November 1= $25.99 USD
    and so on...
 
  Notice that no recurring monthly payment was collected in September, but recurring payments
  were collected roughly every 30 days.
 
  When Monthly Recurring Payments Are Due and Collected on the 30th
  The subscription terms are:
 
    $25.99 USD a month; the subscriber signs up on Tuesday, December 30.
 
  The subscriber is billed as follows:
 
    Tuesday, December 30 = $25.99 USD
    Friday, January 30 = $25.99 USD
    Sunday, March 1= $25.99 USD
    Wednesday, April 1= $25.99USD
    and so on...
 
  Notice that no recurring monthly payment was collected in February, but recurring payments
  were collected roughly every 30 days.
  
https://cms.paypal.com/cms_content/US/en_US/files/developer/PP_WebsitePaymentsStandard_IntegrationGuide.pdf (PDF)

Installation
============

  python setup.py install

Usage
=====

  from paypal_date import get_next_paypal_monthly_billing_date

  today = datetime.datetime.now()

  next_month = get_next_paypal_monthly_billing_date(today)

