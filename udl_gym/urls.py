from django.conf.urls import url, patterns
from django.views.generic import ListView, DetailView
from django.utils import timezone
from models import Activity,Trainers
from . import views


urlpatterns = patterns(
    '',
    # Home
    url(r'^$', views.Home, name='udl_gym'),

    # List activities
    url(r'^Activities/$', ListView.as_view(
        queryset=Activity.objects.order_by('type','name'),
        context_object_name='activity_list',
        template_name = 'templates/activity.html'),
    name='Activities'),

    # Activity detail
    url(r'^Activities/(?P<pk>\d+)/$', DetailView.as_view(
        model=Activity,
        template_name='templates/activity_detail.html'),
        name='Activity_detail'),

    # List trainers
    url(r'^Trainers/$', ListView.as_view(
        queryset=Trainers.objects.order_by('name'),
        context_object_name='trainer_list',
        template_name = 'templates/trainer.html'),
    name='Trainers'),

    # Trainer detail
    url(r'^Trainers/(?P<pk>\d+)/$', DetailView.as_view(
        model=Trainers,
        template_name='templates/trainer_detail.html'),
        name='Trainer_detail'),
)
