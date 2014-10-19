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


class Department(models.Model):
    bm_name = models.CharField(max_length=10)
    bm_leader = models.ManyToMnay(Teacher)
    bm_student = models.ManyToMnay(Student)
    bm_teacher = models.ManyToMnay(Teacher)



# Create your models here.
