from django.db import models

# Create your models here.
class Event(models.Model):

    #id = models.CharField(max_length=140, primary_key=True)
    event_name = models.CharField(max_length=140)
    event_description = models.CharField(max_length=1000)
    event_price = models.DecimalField(max_digits=19, decimal_places=2)
    event_start_date_time = models.DateTimeField()
    event_end_date_time = models.DateTimeField()
    is_syndicated = models.BooleanField(default=False)
