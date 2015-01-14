#-*- coding: utf-8 -*-
# from django.conf import settings
"""for foreignkey of user unused still"""
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# from django.contrib.auth.models import (
#     BaseUserManager, AbstractBaseUser, PermissionsMixin)
# from django.contrib.auth import authenticate


class MyUser(models.Model):
    """user tables"""
    #first part user information
    # uid = models.AutoField(primary_key=True)
    myuser = models.OneToOneField(User, verbose_name="myuser", default=None)
    user_auth_num = models.CharField(max_length=20, default=None)
    real_name = models.CharField(default=None, max_length=50, unique=True, verbose_name="real name")
    telephone = models.CharField(default=None, max_length=50, verbose_name="phone")
    position_choice = (
        ('master', u'所长'),
        ('admin', u'管理员'),
        ('normalmem', u'普通'),
    )
    position = models.CharField(choices=position_choice, max_length=100)
    type_choice = (
        ('teacher', u'教师'),
        ('student', u'学生'),
    )
    sf_type = models.CharField(choices=type_choice, max_length=100)
    group_id = models.IntegerField(default=2)
    group_sf_choice = (
        ('group_master', u'组长'),
        ('group_member', u'组员'),
    )
    group_sf = models.CharField(choices=group_sf_choice, max_length=100)

    def __unicode__(self):
        return self.name

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
    group_name = models.CharField(choices=group_choice, max_length=100)
    group_mem = models.ManyToManyField(MyUser)


class Manageship(models.Model):
    user = models.ForeignKey(MyUser)
    allgroup = models.ForeignKey(AllGroup)
    memtype_choices=(
        ('leader', u'组长'),
        ('member', u'组员'),
    )
    memtype = models.CharField(choices=memtype_choices, max_length=100)
    datejoined = models.DateField()