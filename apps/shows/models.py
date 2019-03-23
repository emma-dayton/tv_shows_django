from __future__ import unicode_literals
from django.db import models
from datetime import datetime, timedelta
# Create your models here.


# validator class, add as attribute to models to validate -- override objects
class ShowManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        present = datetime.now()
        # add keys and values to errors dictionary for each invalid field
        if len(postData['title']) < 1:
            errors["title"] = "Title must be at least 1 character"
        if len(postData['desc']) < 10:
            errors["desc"] = "Show description must be at least 10 characters"
        if int(postData['network']) == 0:
            errors['network'] = 'Please choose the current, or final, network to air this show.'
        if len(postData['debut']) < 1:
            errors['debut'] = 'Please select a date'
        else:
            debut = datetime.strptime(postData['debut'], "%Y-%m-%d")
            if debut > present:
                errors['debut'] = '''Please select a date earlier than today.
                This database is only for shows that are currently on the air,
                not those premiering in the future.'''
            elif int(postData['debut'][0:4]) < 1930:
                errors['debut'] = 'Pick a later date, since television only began airing in the 1930s'
        return errors


# one-to-many, ignoring cases where shows switch networks -- just showing last airing network
class Network(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Show(models.Model):
    title = models.CharField(max_length=255)
    desc = models.TextField()
    debut = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    network = models.ForeignKey(Network, null=True, on_delete=models.SET_NULL)
    objects = ShowManager()
