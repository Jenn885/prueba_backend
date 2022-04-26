from django.db import models
from Jobs.models import Job

# Create your models here.

class Gender(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return str(self.name)

class Employee(models.Model):
    gender_id = models.ForeignKey(Gender, on_delete=models.SET_NULL, null=True)
    job_id = models.ForeignKey(Job, on_delete=models.SET_NULL, null=True)
    name=models.CharField(max_length=255)
    last_name=models.CharField(max_length=255)
    birthdate=models.DateField(null=True)
    def __str__(self):
        return str(self.name)

class WorkedHours(models.Model):
    employee_id = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True)
    worked_hours=models.IntegerField()
    worked_date=models.DateField(null=True)
    
    def __str__(self):
        return str(self.worked_hours)

