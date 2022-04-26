from django.db import models

# Create your models here.

class Job(models.Model):
    name = models.CharField(max_length=255)
    salary=models.DecimalField(max_digits=9, decimal_places=2)
    
    def __str__(self):
        return str(self.name)
