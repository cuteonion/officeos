from django.db import models
from django.utils import timezone


class Teacher(models.Model):

    """teacher models"""
    name = models.CharField(max_length=5)
    age = models.IntegerField()
    sex = models.CharField(max_length=1)
    phone_num = models.CharField(max_length=11)
    email = models.EmailField()
    isleader = models.BooleanField()

    def __unicode__(self):
        return self.name


class Student(models.Model):
    """student models"""
    name = models.CharField(max_length=5)
    age = models.IntegerField()
    sex = models.CharField(max_length=1)
    phone_num = models.CharField(max_length=11)
    email = models.EmailField()

    def __unicode__(self):
        return self.name


class Department(models.Model):
    bm_name = models.CharField(max_length=10)
    bm_student = models.ManyToManyField(Student, through='Studeship')
    bm_teacher = models.ManyToManyField(Teacher, through='Teadeship')
    bm_person_num = models.IntegerField()
    bm_leader = models.ForeignKey(Teacher)

    def __unicode__(self):
        return self.bm_name


class Studeship(models.Model):
    student = models.ForeignKey(Student)
    department = models.ForeignKey(Department)
    join_time = models.DateTimeField(default=timezone.now())



class Teadeship(models.Model):
    teacher = models.ForeignKey(Teacher)
    department = models.ForeignKey(Department)
    join_time = models.DateTimeField(default=timezone.now())



















# Create your models here.
