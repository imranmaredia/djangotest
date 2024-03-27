from django.db import models

# Create your models here.


class Task(models.Model):
    firstname = models.CharField(max_length=500)
    lastname = models.CharField(max_length=500)
    waaratype = models.CharField(max_length=500)
    PlaceHolder = models.CharField(max_length=500)
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

def __str__(self):
    return self.firstname 
