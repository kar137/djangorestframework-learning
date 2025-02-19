from django.db import models
from datetime import datetime

# Create your models here.

class comment(models.Model):
    email = models.EmailField(max_length=200)
    name = models.CharField(max_length=200)
    date = models.DateField()

class Student(models.Model):
    title = models.CharField(max_length=100, default="student")
    roll_no = models.IntegerField(unique=True, null=False)
    name = models.CharField(max_length=100, null=False)
    department = models.CharField(max_length=100, null= True)
    address = models.CharField(max_length=100)
    start_date = models.DateField(auto_now_add=True)
    end_date = models.DateField(blank=True, null=True)
    
    
    
    
    



    
