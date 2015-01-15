#-*- coding: utf-8 -*-
# from django.conf import settings
"""for foreignkey of user unused still"""
from django.db import models
from django.contrib.auth.models import User
# from project.models import Project
from django.utils import timezone



class MyUser(models.Model):
    """user tables"""
    #first part user information
    # uid = models.AutoField(primary_key=True)
    myuser = models.OneToOneField(User, verbose_name="myuser", default=None)
    user_auth_num = models.CharField(max_length=20, default=None, verbose_name=u'证件号码')
    real_name = models.CharField(default=None, max_length=50, unique=True, verbose_name=u"姓名")
    telephone = models.CharField(default=None, max_length=11, verbose_name=u"联系方式")
    position_choice = (
        ('master', u'所长'),
        ('admin', u'管理员'),
        ('normalmem', u'普通'),
    )
    position = models.CharField(choices=position_choice, verbose_name=u'职位', max_length=100)
    type_choice = (
        ('teacher', u'教师'),
        ('student', u'学生'),
    )
    sf_type = models.CharField(choices=type_choice, verbose_name=u'身份', max_length=100)
    group_id = models.IntegerField(default=2, verbose_name=u'研究组编号')
    group_sf_choice = (
        ('group_master', u'组长'),
        ('group_member', u'组员'),
    )
    group_sf = models.CharField(choices=group_sf_choice, max_length=100)

    def __unicode__(self):
        return self.real_name

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
    group_name = models.CharField(verbose_name="组名", max_length=100, db_column='group_name')
    group_mem = models.ManyToManyField(MyUser)

    def __str__(self):
        return self.group_name

class Manageship(models.Model):
    user = models.ForeignKey(MyUser)
    allgroup = models.ForeignKey(AllGroup)
    memtype_choices=(
        ('leader', u'组长'),
        ('member', u'组员'),
    )
    memtype = models.CharField(choices=memtype_choices, max_length=100,verbose_name=u'组身份')
    datejoined = models.DateField(verbose_name=u'创建日期')

    def __str__(self):
        return self.user.real_name + " in "+ self.allgroup.group_name