from django.db import models

# Create your models here.
class Person(model.Model):
    firstname = model.CharField(max_length=30)
    lastname  = model.CharField(max_length=30)
