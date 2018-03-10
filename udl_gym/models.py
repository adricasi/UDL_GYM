from django.db import models
from django.core.urlresolvers import reverse


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
        return reverse('About us', kwargs={'pk': self.pk})

class Activity(models.Model):
    name = models.TextField()
    description = models.TextField(blank=True, null=True)
    type = models.TextField()


    def __unicode__(self):
        return u"%s" % self.name

    def get_absolute_url(self):
        return reverse('udl_gym:activity_detail',
                       kwargs={'pk': self.pk})


class Trainers(models.Model):
    name = models.TextField()
    street = models.TextField(blank=True, null=True)
    telephone = models.IntegerField(blank=True, null=True)
    city = models.TextField(blank=True, null=True)
    state_or_province = models.TextField(blank=True, null=True)
    country = models.TextField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    specialized = models.TextField(blank=True, null=True)


    def __unicode__(self):
        return u"%s" % self.name

    def get_absolute_url(self):
        return reverse('udl_gym:Trainers_detail',
                       kwargs={ 'pk': self.pk})