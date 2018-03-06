from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from datetime import date

# Create your models here.
class Gym(models.Model):
    name = models.TextField()
    street = models.TextField(blank=True, null=True)
    telephone = models.IntegerField(blank=True, null=True)
    city = models.TextField(blank=True, null=True)
    state_or_province = models.TextField(blank=True, null=True)
    country = models.TextField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    url = models.URLField(blank=True, null=True)

    # Aclarir tema claus primaries i foranees

    def __unicode__(self):
        return u"%s" % self.name

    def get_absolute_url(self):
        return reverse('udl_gym:About_us', kwargs={'pk': self.pk})

class Activity(models.Model):
    name = models.TextField()
    description = models.TextField(blank=True, null=True)
    type = models.TextField()
    gym = models.ForeignKey(Gym, null=True, related_name='activities')
    date = models.DateField(default=date.today)

    def __unicode__(self):
        return u"%s" % self.name

    def get_absolute_url(self):
        return reverse('udl_gym:activity_detail',
                       kwargs={'pkr': self.gym.pk, 'pk': self.pk})


class Trainers(models.Model):
    name = models.TextField()
    street = models.TextField(blank=True, null=True)
    telephone = models.IntegerField(blank=True, null=True)
    city = models.TextField(blank=True, null=True)
    state_or_province = models.TextField(blank=True, null=True)
    country = models.TextField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    specialized = models.TextField(blank=True, null=True)
    gym = models.ForeignKey(Gym, null=True, related_name='trainers')

    def __unicode__(self):
        return u"%s" % self.name

    def get_absolute_url(self):
        return reverse('udl_gym:Trainers_detail',
                       kwargs={'pkr': self.gym.pk, 'pk': self.pk})