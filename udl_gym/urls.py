from django.conf.urls import url, patterns
from django.views.generic import ListView
from django.utils import timezone
from models import Activity
from . import views

urlpatterns = patterns(
    '',
    #Home
    url(r'^$', views.Home, name='udl_gym'),

    #List activities
    url(r'^Activities/$', ListView.as_view(
        queryset=Activity.objects.filter(date__lte=timezone.now()).order_by('date'),context_object_name='Activity',template_name = '../templates/activity.html'),
    name='Activities'),

    #Activity detail
)
