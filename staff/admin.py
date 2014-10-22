#-*- coding: utf-8 -*-

from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from staff.models import Staffuser, Department, Staffship


class StaffuserInline(admin.StackedInline):
    model = Staffuser
    verbose_name_plural = 'staff'

class UserAdmin(UserAdmin):
    search_fields = ('username',)
    # fieldsets = [
    #     (u'基本信息', {'fields':['username', 'password']}),
    # ]
    inlines = (StaffuserInline, )
admin.site.unregister(User)
admin.site.register(Department)
admin.site.register(Staffship)
admin.site.register(User, UserAdmin)
admin.site.register(Staffuser)

#about xadmin
# xadmin.site.unregister(User)

# Register your models here.
