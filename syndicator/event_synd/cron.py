
from .models import Event
from .api_functions import post_to_ThisWeek, post_to_NiftyNYC, post_to_Newsday

def syndicator():
    events = Event.objects.get(is_syndicated=False)
    if events:
        for event in events:
            '''
            data = {
                'event.name.html': event.event_name,
                'event.description.html': event.event_description,
                'event.start.utc': event.event_start_date_time,
                'event.start.timezone': event.event_timezone,
                'event.end.utc': event.event_end_date_time,
                'event.end.timezone': event.event_timezone,
                'event.currency': event.event_currency
            }
            '''
            post_to_ThisWeek(event)
            resp1 = post_to_NiftyNYC(event)
            resp2 = post_to_Newsday(event)
            event.is_syndicated = True
            event.save()
    else:
        print 'No new events found'
    pass

