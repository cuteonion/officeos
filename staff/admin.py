#-*- coding: utf-8 -*-
from django import forms
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from staff.models import MyUser
"""import something"""


class UserCreateForm(forms.ModelForm):
    """form for create user"""
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='Password confirmation',
        widget=forms.PasswordInput
        )
    class Meta:
        model = User
        fields = ('login_name', 'name', 'email', 'telephone', 'position')

    def clean_password2(self):
        """cheack if the passwords are same"""
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1!=password2:
            raise forms.ValidationError("Passwords dont'match.")
        return password2

    def save(self, commit=True):
        """save the provided password as hash"""
        user = super(UserCreateForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
            return user


class UserChangeForm(forms.ModelForm):
    """form for change information of users"""
    password = ReadOnlyPasswordHashField()

    class Meta:
        models = MyUser
        fields = (
            'login_name', 'name', 'email', 'telephone', 'position', )

    def clean_password(self):
        return self.initial["password"]


class MyUserAdmin(UserAdmin):
    """forms to add or change MyUser instance"""
    form = UserChangeForm
    add_form = UserCreateForm
    """the fields to used displaying"""
    list_display = ('name', 'login_name', 'email', 'telephone', 'position')
    fieldsets = (
        (None, {'fields': ('login_name', 'password')}),
        ('Peronalinfo', {'fields': ('name', 'email', 'telephone', )}),
        ('Permissions', {
            'fields': (
                'is_boss', 'is_admin', 'is_leader', 'is_teacher', 'is_student')
            }),
        )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'name', 'login_name', 'email', 'telephone',
                'position', 'password1', 'password2')}),
    )

    search_fields = ('name', 'login_name', 'email')
    ordering = ('name')
    filter_horizontal = ()


    #register the objects
    admin.site.register(MyUser, MyUserAdmin)
    admin.site.unregiester(Group)









































# import xadmin



# class StaffuserInline(admin.StackedInline):
#     model = Staffuser
#     verbose_name_plural = 'staff'

# class UserAdmin(UserAdmin):
#     search_fields = ('username',)

#     # fieldsets = [
#     #     (u'基本信息', {'fields':['username', 'password']}),
#     # ]
#     inlines = (StaffuserInline, )


# class DepartmentAdmin(admin.ModelAdmin):
#     fieldsets = (
#         (None, {'fields': ('name', 'staffs', )}),
#         )


# class StaffshipAdmin(admin.ModelAdmin):
#     fields = ('department', 'staff', 'is_leader')


# admin.site.unregister(User)
# admin.site.register(User, UserAdmin)

# admin.site.register(Department, DepartmentAdmin)
# admin.site.register(Staffship, StaffshipAdmin)
# admin.site.register(Staffuser)

#about xadmin
# xadmin.site.unregister(User)

# Register your models here.
