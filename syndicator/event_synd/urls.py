from django.conf.urls import include, url
from django.views.generic import TemplateView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from .views import EventFormView, ObjectsView

urlpatterns = [
    url(r'home', EventFormView.as_view(), name='index'),
    url(r'objects', ObjectsView.as_view(), name='objects'),
]