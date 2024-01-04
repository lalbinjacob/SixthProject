from django.db import models
from django.shortcuts import render


# Create your models here.
class Purpose(models.Model):
    name=models.CharField(max_length=250)
    def __str__(self):
        return self.name


class Department(models.Model):
    name=models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Course(models.Model):
    department=models.ForeignKey(Department,on_delete=models.CASCADE)
    name=models.CharField(max_length=50)
    def __str__(self):
        return self.name


class Ordering(models.Model):

    name=models.CharField(max_length=250)
    birthdate=models.DateField(null=True)
    gender=models.CharField(max_length=100,null=True)
    age=models.PositiveIntegerField(null=True)
    phone_number=models.CharField(max_length=11,null=True)
    email=models.EmailField(max_length=200)
    address=models.CharField(max_length=250)
    department=models.ForeignKey(Department,on_delete=models.SET_NULL,null=True)
    course=models.ForeignKey(Course,on_delete=models.SET_NULL,null=True)
    purpose=models.ForeignKey(Purpose,on_delete=models.SET_NULL,null=True)
    materials_provide=models.CharField(max_length=200,null=True)


    def __str__(self):
        return self.name


