from django.db import models

# Create your models here.
class Search(models.Model):
    search = models.CharField(max_length=500) #does not exceed more than 500 char
    created = models.DateTimeField(auto_now=True)  #date auto stamps