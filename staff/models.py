#-*- coding: utf-8 -*-
# from django.confimport settings
"""for foreignkey of user unused still"""
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser, PermissionsMixin
    )


class UserManager(BaseUserManager):
    def create_user(
        self, login_name, name, email, telephone, position, password=None
            ):
        """
        create and save a User with given email
        """
        if not (login_name or name or email or telephone or position):
            raise ValueError('all the information is needed.')
        user = self.model(
            login_name=login_name,
            name=name,
            email=self.normalize_email(email),
            telephone=telephone,
            position=position_choice,
            )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(
        self, login_name, name, email, telephone, position, password
            ):
            user = create_user(login_name, name, email, telephone, position)
            user.is_admin = True
            user.save(using=self._db)


class MyUser(AbstractBaseUser, PermissionsMixin):
    """user tables"""

    login_name = models.CharField(
        pk=True, max_length=50, unique=True, verbose_name="login name")
    name = models.CharField(
        max_length=50, unique=True, verbose_name="name")
    email = models.EmailField(
        max_length=50, unique=True, verbose_name="email adress")
    telephone = models.CharField(max_length=50, verbose_name="phone")
    position_choice = [u'所长', u'管理员', u'组长', u'教师', u'学生']
    position = models.CharField(position_choice=position_choice)
    last_login = models.DateTimeField()

    is_active = models.BooleanField(default=True)
    is_delete = models.BooleanField(default=False)
    is_student = models.BooleanField(default=True)
    # is_part_leader = models.BooleanField(default=False)
    # is_boss = models.BooleanField(default=False)
    # is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'login_name'
    REQUIRED_FIELDS = ['email']

    def get_full_name(self):
        return self.name

    def __unicode__(self):
        return self.login_name

    def has_perm(self, perm, obj=None):
        return True

    @property
    def is_boss(self):
        if self.position == u'所长':
            return True
        else:
            return False

    def is_admin(self):
        if self.position == u'管理员':
            return True
        else:
            return False

    def is_zuzhang(self):
        if self.position == u'组长':
            return True
        else:
            return False

    def is_teacher(self):
        if self.position == u'教师':
            return True
        else:
            return False


class Department(models.Model):
    department_id = models.IntegerField(Auto=True, primary_key=True)
    staff = models.ManyToManyField(through='Staffship')
    name = models.CharField(max_length=50)

    @property
    def leader(self):
        return self.staff.objects.get(is_leader=True).name

class Staffship(models.Model):
    """staffship"""
    staff = models.ForeignKey(MyUser)
    department = models.ForeignKey(Department)

    @property
    def position(self):
        return self.staff.position





































class MyUser(User):



# class Staffuser(models.Model):
#     """extend the model User"""

#     staff_type_choice = {
#         ('teacher', u'教师'),
#         ('student', u'学生'),
#     }
#     objects = models.Manager()
#     user = models.OneToOneField(User)
#     name = models.CharField(
#         max_length=50, blank=False, null=True, verbose_name=u'姓名')
#     mobile = models.CharField(
#         max_length=50, blank=False, null=True, verbose_name=u'手机')
#     create_at = models.DateTimeField(auto_now_add=True, verbose_name=u'创建时间')
#     staff_type = models.CharField(
#         max_length=100, choices=staff_type_choice, verbose_name=u'人员身份')

#     def __unicode__(self):
#         return self.staff_type+':'+self.name

# class Department(models.Model):
#     '''研究室'''
#     department_choice = {
#         ('A', u'研究室A'),
#         ('B', u'研究室B'),
#         ('C', u'研究室C'),
#     }
#     name = models.CharField(
#         choices=department_choice, max_length=100, verbose_name=u'研究室')
#     staffs = models.ManyToManyField(User, verbose_name=u'研究室人员')
#     department_id = models.IntegerField(primary_key=True)
#     # staff_num = models.IntegerField(verbose_name=u'研究室人数')

#     def __unicode__(self):
#         return self.name


# class Staffship(models.Model):
#     department = models.ForeignKey(Department, verbose_name=u'研究室')
#     staff = models.ForeignKey(Staffuser)
#     is_leader = models.BooleanField(default=False)
#     ship_id = models.IntegerField(primary_key=True)

#     def __unicode__(self):
#         return self.staff.name+'is in '+self.department.name



# class Teacher(models.Model):

#     """teacher models"""
#     objects = models.Manager()
#     name = models.CharField(max_length=5)
#     age = models.IntegerField()
#     sex = models.CharField(max_length=1)
#     phone_num = models.CharField(max_length=11)
#     email = models.EmailField()
#     isleader = models.BooleanField(defaul=False)

#     def leadwhichdepart(self):
#         """get the department the teacher leads"""
#         if self.isleader is True:
#             instance = Teadeship.objects.get(teacher=self.name)
#             return instance.department

#     def add_mem(self, position, name, age, sex, phone_num, email):
#         """to add memebers,students or teacher"""
#         if self.isleader is True:
#             departmentname = self.leadwhichdepart()
#             department = Department.objects.get(bm_name=departmentname)
#             if position is 'teacher':
#                 teaadd = Teacher.objects.create(
#                     name=name,
#                     age=age,
#                     sex=sex,
#                     phone_num=phone_num,
#                     email=email,
#                     isleader=False
#                     )
#                 teaadd.save()

#                 teadeship = Teadeship.objects.create(
#                     teacher=teaadd,
#                     department=department,
#                     join_time=timezone.now()

#                     )
#                 teadeship.save()

#             elif position is 'student':
#                 stuadd = Teacher.objects.create(
#                     name=name,
#                     age=age,
#                     sex=sex,
#                     phone_num=phone_num,
#                     email=email,
#                     isleader=False
#                     )
#                 stuadd.save()
#                 studeship = Studeship.objects.create(
#                     student=stuadd,
#                     department=department,
#                     join_time=timezone.now()

#                     )
#                 studeship.save()


#     def __unicode__(self):
#         return self.name


# class Student(models.Model):
#     """student models"""
#     objects = models.Manager()
#     name = models.CharField(max_length=5)
#     age = models.IntegerField()
#     sex = models.CharField(max_length=1)
#     phone_num = models.CharField(max_length=11)
#     email = models.EmailField()

#     def __unicode__(self):
#         return self.name


# class Department(models.Model):
#     objects = models.Manager()
#     bm_name = models.CharField(max_length=10)
#     bm_student = models.ManyToManyField(Student, through='Studeship')
#     bm_teacher = models.ManyToManyField(Teacher, through='Teadeship')
#     bm_person_num = models.IntegerField()

#     def leader(self, teacher):
#         """to return the leader of the department"""
#         instance = Teadeship.objects.get(
#             department=self.bm_name, teacher=teacher)
#         leader = Teacher.objects.get(name=instance.teacher)
#         if leader.isleader is True:
#             return teacher

#     def __unicode__(self):
#         return self.bm_name


# class Studeship(models.Model):
#     objects = models.Manager()
#     student = models.ForeignKey(Student)
#     department = models.ForeignKey(Department)
#     join_time = models.DateTimeField(default=timezone.now())


# class Teadeship(models.Model):
#     objects = models.Manager()
#     teacher = models.ForeignKey(Teacher)
#     department = models.ForeignKey(Department)
#     join_time = models.DateTimeField(default=timezone.now())



















# # # Create your models here.
