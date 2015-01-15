#-*- coding: utf-8 -*-
from django.db import models
from staff.models import MyUser


class StartProject(models.Model):
    startpro_id = models.AutoField(primary_key=True, verbose_name=u"项目编号")
    startpro_name = models.CharField(max_length=100, verbose_name=u"项目名称")
    startpro_starter = models.CharField(max_length=100, verbose_name=u'项目发起人')
    startpro_status_choices = (
        ('start', u'待审核'),
        ('checked', u'审核通过'),
    )
    startpro_start_date = models.DateField(verbose_name=u'项目发起日期')
    startpro_cost = models.CharField(max_length=100, verbose_name=u'花费预算')
    startpro_comment = models.TextField(max_length=1000, verbose_name=u'项目描述')
    def __str__(self):
        return self.project_name


class WorkProject(models.Model):
    project_id = models.AutoField(primary_key=True, verbose_name=u"项目编号")
    project_name = models.CharField(max_length=100, verbose_name=u"项目名称")
    project_start_date = models.DateField(verbose_name=u'项目发起日期')
    project_work_date = models.DateField(verbose_name=u'项目执行日期')
    project_end_date = models.DateField(verbose_name=u'项目结束日期')
    project_status_choices = (
        ('checked', u'审核通过'),
        ('upload', u'上传资料'),
        ('working', u'进行中'),
        ('finish', u'完成'),
        ('abandon', u'放弃'),
    )
    project_status = models.CharField(
        max_length=100,
        choices=project_status_choices,
        verbose_name=u'项目状态'
    )
    project_leader = models.CharField(max_length=100, verbose_name=u'项目负责人')
    project_mem = models.ManyToManyField(MyUser, verbose_name=u'项目组成员')
    project_cost = models.CharField(default=None, max_length=100, verbose_name=u'项目费用')
    def __str__(self):
        return  self.project_name


class ProAndUserShip(models.Model):
    project_mem = models.ForeignKey(MyUser)
    project = models.ForeignKey(WorkProject)

    def __str__(self):
        return self.WorkProject.project_name + '(' + u'发起人:' +self.WorkProject.project_leader + ')'
