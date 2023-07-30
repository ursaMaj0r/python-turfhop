import requests
import json
from thapi import *

def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

def customers():
    customers = Customer().all()
    for customer in customers:
        jprint(customer)

def customer_satisfaction():
    customers = Customer(type="Homeowner").all()
    for customer in customers:
        print("{}, {}".format(customer['Name'],customer['SurveyOverallSatisfaction']))
       
def job_lot_size():
    jobs = Job().all()
    for job in jobs:
        info = Job(job['Id']).info()
        print("{}, {} acres".format(info['JobAddress'],info['LotSize']))
   
def job_visits_per_invoice():
    jobs = Job().all()
    for job in jobs:
        info = Job(job['Id']).info()
        print("{}, {} Visits, {} Invoices, {}% Invoiced".format(info['JobAddress'],info['NumberOfVisits'],info['NumberOfInvoices'],(info['NumberOfVisits']/info['NumberOfInvoices']*100)))        

def overdue_invoices():
    invoices = Invoice(subStatus="Overdue").all()
    print("Total Overdue Invoices: {}".format(len(invoices)))
    for invoice in invoices:
        print("{} owes {}. The invoice is {} days old and the service was completed on {}.".format(Customer(invoice['CustomerId']).info()['Name'],invoice['Balance'],invoice['Age'],invoice['ServiceDates']))
 
def employee_time_logs():
    employees = Employee().all()
    for employee in employees:
        info = Employee(employee['Id']).time_logs()
        print(info)      