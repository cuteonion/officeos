from django.db import models
from django.utils import timezone


class Teacher(models.Model):

    """teacher models"""
    objects = models.Manager()
    name = models.CharField(max_length=5)
    age = models.IntegerField()
    sex = models.CharField(max_length=1)
    phone_num = models.CharField(max_length=11)
    email = models.EmailField()
    isleader = models.BooleanField(defaul=False)

    def leadwhichdepart(self):
        """get the department the teacher leads"""
        if self.isleader is True:
            instance = Teadeship.objects.get(teacher=self.name)
            return instance.department

    def add_mem(self, position, name, age, sex, phone_num, email):
        if self.isleader is True:
            departmentname = self.leadwhichdepart()
            department = Department.objects.get(bm_name=departmentname)
            if position is 'teacher':
                teaadd = Teacher.objects.create(
                    name=name,
                    age=age,
                    sex=sex,
                    phone_num=phone_num,
                    email=email,
                    isleader=False
                    )
                teaadd.save()

                teadeship = Teadeship.objects.create(
                    teacher=teaadd,
                    department=department,
                    join_time=timezone.now()

                    )
                teadeship.save()

            elif position is 'student':
                stuadd = Teacher.objects.create(
                    name=name,
                    age=age,
                    sex=sex,
                    phone_num=phone_num,
                    email=email,
                    isleader=False
                    )
                stuadd.save()
                studeship = Studeship.objects.create(
                    student=stuadd,
                    department=department,
                    join_time=timezone.now()

                    )
                studeship.save()


    def __unicode__(self):
        return self.name


class Student(models.Model):
    """student models"""
    objects = models.Manager()
    name = models.CharField(max_length=5)
    age = models.IntegerField()
    sex = models.CharField(max_length=1)
    phone_num = models.CharField(max_length=11)
    email = models.EmailField()

    def __unicode__(self):
        return self.name


class Department(models.Model):
    objects = models.Manager()
    bm_name = models.CharField(max_length=10)
    bm_student = models.ManyToManyField(Student, through='Studeship')
    bm_teacher = models.ManyToManyField(Teacher, through='Teadeship')
    bm_person_num = models.IntegerField()

    def leader(self, teacher):
        """to return the leader of the department"""
        instance = Teadeship.objects.get(
            department=self.bm_name, teacher=teacher)
        leader = Teacher.objects.get(name=instance.teacher)
        if leader.isleader is True:
            return teacher

    def __unicode__(self):
        return self.bm_name


class Studeship(models.Model):
    objects = models.Manager()
    student = models.ForeignKey(Student)
    department = models.ForeignKey(Department)
    join_time = models.DateTimeField(default=timezone.now())


class Teadeship(models.Model):
    objects = models.Manager()
    teacher = models.ForeignKey(Teacher)
    department = models.ForeignKey(Department)
    join_time = models.DateTimeField(default=timezone.now())



















# # Create your models here.
