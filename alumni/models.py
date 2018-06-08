from django.db import models

# Create your models here.
class Student(models.Model):
    first_name = models.CharField(null=True, max_length=50)
    last_name = models.CharField(null=True, max_length=50)
    phone = models.CharField(null=True, max_length=50)
    email = models.CharField(null=True, max_length=50)
    grad_year = models.IntegerField(null=True)
