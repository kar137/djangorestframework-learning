from django.db import models
from datetime import datetime

# Create your models here.

class comment(models.Model):
    email = models.EmailField(max_length=200)
    name = models.CharField(max_length=200)
    date = models.DateField()

class Student(models.Model):
    roll_no = models.IntegerField(unique=True, null=False)
    name = models.CharField(max_length=100, null=False)
    department = models.CharField(max_length=100, null= True)
    address = models.CharField(max_length=100)
    
    
    
    
    



    
