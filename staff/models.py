#-*- coding: utf-8 -*-
# from django.conf import settings
"""for foreignkey of user unused still"""
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser, PermissionsMixin)
from django.contrib.auth import authenticate

class UserManager(BaseUserManager):
    def _create_user(
        self, login_name, email, password, is_superuser, is_staff, group_id):
        """
        create and save a User with given email
        """
        now = timezone.now()
        if not (login_name):
            raise ValueError('all the information is needed.')
        user = self.model(
            login_name=login_name,
            email=self.normalize_email(email),
            is_superuser=is_superuser,
            is_staff=is_staff,
            # name=name,
            # telephone=telephone,
            # position=position,
            last_login = now,
            group_id=group_id,
            )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(
            self, login_name, email=None, password=None, group_id=2):
        return self._create_user(login_name, email, password,  False, True, group_id)

    def create_superuser(
            self, login_name, email, password=None, group_id=1):
        return self._create_user(login_name, email, password, True, True, group_id )


class MyUser(AbstractBaseUser, PermissionsMixin):
    """user tables"""
    #first part user information
    user_id = models.AutoField(primary_key=True)
    user_auth_num = models.CharField(max_length=10)
    login_name = models.CharField(
        max_length=50, unique=True,
        verbose_name="login name")
    name = models.CharField(
        max_length=50, unique=True, verbose_name="name")
    email = models.EmailField(
        max_length=50, unique=True, verbose_name="email address")
    telephone = models.CharField(max_length=50, verbose_name="phone")
    #second part user's position and user type
    position_choice = (
        ('master', u'所长'),
        ('admin', u'管理员'),
        ('normalmem', u'普通'),
    )
    position = models.CharField(choices=position_choice, max_length=10)
    type_choice = (
        ('teacher', u'教师'),
        ('student', u'学生'),
    )
    sf_type = models.CharField(choices=type_choice, max_length=10)
    #third part user's groups
    group_id = models.IntegerField(default=2)
    group_sf_choice = (
        ('group_master', u'组长'),
        ('group_member', u'组员'),
    )
    group_sf = models.CharField(choices=group_sf_choice, max_length=10)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_delete = models.BooleanField(default=False)
    # is_part_leader = models.BooleanField(default=False)
    # is_boss = models.BooleanField(default=False)
    # is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'login_name'
    REQUIRED_FIELDS = ['email', ]

    """when try to import user profile information,
    this fields must be modified to suite the
    exiting file's columns.
    so that the behavior can be completed
    """
    def __unicode__(self):
        return self.name

    def get_full_name(self):
        """the real name"""
        return self.name

    def has_perm(self, perm, obj=None):
        """if has the Permissions"""
        return True

    @property
    def is_boss(self):
        """boss"""
        if self.position == u'所长':
            return True
        else:
            return False

    def is_admin(self):
        """admin"""
        if self.position == u'管理员':
            return True
        else:
            return False

    def is_teacher(self):
        """is teacher or not"""
        if self.sf_type == u'教师':
            return True
        else:
            return False
    def is_student(self):
        """is student or not"""
        if self.sf_type == u'学生':
            return True
        else:
            return False


class AllGroup(models.Model):
    group_id = models.AutoField(primary_key=True, db_column='allgroup_id')
    group_choice = (
        ('manage_group', u'管理组'),
        ('study_group1', u'研究组1'),
        ('study_group2', u'研究组2'),
    )
    group_name = models.CharField(choices=group_choice, max_length=10)
    group_mem = models.ForeignKey(MyUser)



# class Department(models.Model):
#     """department"""
#     department_id = models.AutoField(primary_key=True)
#     staff = models.ManyToManyField(MyUser, through='Staffship')
#     name = models.CharField(max_length=50)

#     @property
#     def leader(self):
#         """get the leader of the department"""
#         return self.staff.objects.get(is_leader=True).name



#     @property
#     def position(self):
#         """return the position of the user in the ship"""
#         return self.staff.position

