from django.db import models

# Create your models here.

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
