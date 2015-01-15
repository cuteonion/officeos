#-*- coding: utf-8 -*-
# from django.contrib import admin
from project.models import StartProject, WorkProject, ProAndUserShip# Re-register UserAdmin
import xadmin


xadmin.site.register(StartProject)
xadmin.site.register(WorkProject)
xadmin.site.register(ProAndUserShip)
