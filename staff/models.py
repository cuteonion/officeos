from django.db import models


class Teacher(models.Model):
    """teacher models"""
    name = models.CharField(max_length=5)
    age = models.IntegerField()
    sex = models.CharField(max_length=1)
    phone_num = models.CharField(max_length=11)
    email = models.EmailField()



class Student(models.Model):
    """student models"""
    name = models.CharField(max_length=5)
    age = models.IntegerField()
    sex = models.CharField(max_length=1)
    phone_num = models.CharField(max_length=11)
    email = models.EmailField()




# Create your models here.
