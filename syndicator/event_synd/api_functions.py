import requests
import urllib
from django.core.mail import send_mail

'''
def post_to_Eventbrite(data):
    endpoint_url = 'https://www.eventbriteapi.com/v3/events/'
    headers = {
        'Authorization': 'Bearer 3DIPRSC4QWG6T6OSFVIA'
    }
    response = requests.post(endpoint_url, data=data, headers=headers)
    return response
'''

def post_to_ThisWeek(event):
    subject = event.event_name
    message = ('Title: ' + event.event_name + 
    '\nDescription: ' + event.event_description + 
    '\nAddress: ' + event.event_address +
    '\nPrice: ' + event.event_currency + ' ' + event.event_price +
    '\nFrom: ' + event.event_start_date_time +
    '\nTo: ' + event.event_end_date_time +
    '\nTime-zone: ' + event.event_time_zone)
    send_mail(subject, 
    message, 
    'test@example.com', 
    ['thisweek.ny@timeout.com'],
    fail_silently=False 
    )

def post_to_NiftyNYC(event):
    url = 'www.niftynyc.com/submit-event/'
    start = event.event_start_date_time.split(',')
    end = event.event_end_date_time.split(',')
    dates = start[0] + '-' + end[0]
    times = start[1] + '-' + end[1]
    cost = event.event_currency + ' ' + event.event_price
    payload = {
        'ninja_forms_field_6': event.event_name,
        'ninja_forms_field_8': dates,
        'ninja_forms_field_11': times,
        'ninja_forms_field_9': event.event_address,
        'ninja_forms_field_12': cost,
        'ninja_forms_field_17': event.event_description,
        'ninja_forms_field_18': 'Pulsd',
        'ninja_forms_field_19': 'test@example.com'
    }
    response = requests.post(url, payload)
    return response

def post_to_Newsday(event):
    url = 'https://www.newsday.com/user-content/submit-an-event-1.1992168'
    start = event.event_start_date_time.split(',')
    timeframe = event.event_start_date_time + 'to ' + event.event_end_date_time
    cost = event.event_currency + ' ' + event.event_price
    payload = {
        'fname': 'Pulsd',
        'lname': 'Admin',
        'email': 'test@example.com',
        'phone': '1234567890',
        'eventname': event.event_name,
        'eventdescription': event.event_description,
        'eventphone1': '1234567890',
        'eventadmission': cost,
        'venuename': event.event_address,
        'venuecity': 'New York City',
        'venueaddress': event.event_address,
        'state': 'New York',
        'zip': '07023',
        'eventdate_1': start[0],
        'additionaldatesinfo_1': timeframe
    }
    response = requests.post(url, payload)
    return response