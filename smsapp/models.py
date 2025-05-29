from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField( max_length=100)
    classname = models.CharField(max_length=100)
    
   

    def __str__(self):
        return f"{self.name} {self.classname}"


class Courses(models.Model):
    coarsecode= models.CharField( default='SM000' , max_length=100)
    coarsename = models.CharField(max_length=100)
    duration = models.CharField(max_length=100)
    fees = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.coarsename