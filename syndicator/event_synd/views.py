from django.shortcuts import render, render_to_response
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import View, TemplateView, FormView
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, get_user_model, login, logout

from .models import Event
from .forms import AddEventForm

import datetime as dt

# Create your views here.
class EventFormView(View):
    
    form_class = AddEventForm
    template_name = 'event_synd/index.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        context = {
            'form': form 
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            clean = form.cleaned_data
            eventname = clean['name']
            description = clean['description']
            currency = clean['currency']
            price = clean['price']
            start_date = clean['start_date']
            start_time = clean['start_time']
            #start_time = dt.datetime.strptime(clean['start_time'], '%H%M').time()
            end_date = clean['end_date']
            end_time = clean['end_time']
            #end_time = dt.datetime.strptime(clean['end_time'], '%H%M').time()
            timezone = clean['timezone']
            
            event_object, created = Event.objects.get_or_create(
                event_name = eventname,
                event_description = description,
                event_currency = currency,
                event_price = price,
                event_start_date_time = dt.datetime.combine(start_date, start_time),
                event_end_date_time = dt.datetime.combine(end_date, end_time),
                event_time_zone = timezone
            )

            if created:
                try:
                    event_object.save()
                except Exception as e:
                    return HttpResponseRedirect(reverse('index'))
            else:
                event_object.is_syndicated = False
                event_object.save()
            
            return HttpResponseRedirect(reverse('index'))

class ObjectsView(View):

    template_name = 'event_synd/objects.html'

    def get(self, request, *args, **kwargs):
        events = Event.objects.all()
        context = {
            'events': events
        }
        return render(request, self.template_name, context)

