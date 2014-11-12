#-*- coding: utf-8 -*-
# from django.confimport settings
"""for foreignkey of user unused still"""
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser, PermissionsMixin
    )
from django.contrib.auth import authenticate

class UserManager(BaseUserManager):
    def create_user(
        self, login_name, name, email, telephone, position, password=None,
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
            position=position,
            )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(
        self, login_name, name, email, telephone, position, password,
            ):
            user = create_user(login_name, name, email, telephone, position)
            user.is_admin = True
            user.save(using=self._db)


class MyUser(AbstractBaseUser, PermissionsMixin):
    """user tables"""
    user_id = models.AutoField(primary_key=True)
    login_name = models.CharField(
        max_length=50, unique=True,
        verbose_name="login name")
    name = models.CharField(
        max_length=50, unique=True, verbose_name="name")
    email = models.EmailField(
        max_length=50, unique=True, verbose_name="email adress")
    telephone = models.CharField(max_length=50, verbose_name="phone")
    position_choice = [u'所长', u'管理员', u'组长', u'教师', u'学生']
    position = models.CharField(choices=position_choice)
    last_login_date = models.DateTimeField()

    is_active = models.BooleanField(default=True)
    is_delete = models.BooleanField(default=False)
    # is_part_leader = models.BooleanField(default=False)
    # is_boss = models.BooleanField(default=False)
    # is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'login_name'
    REQUIRED_FIELDS = ['email']

    def __unicode__(self):
        return self.login_name

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

    def is_zuzhang(self):
        """is department leader or not"""
        if self.position == u'组长':
            return True
        else:
            return False

    def is_teacher(self):
        """is teacher or not"""
        if self.position == u'教师':
            return True
        else:
            return False


# class Department(models.Model):
#     """department"""
#     department_id = models.AutoField(primary_key=True)
#     staff = models.ManyToManyField(MyUser, through='Staffship')
#     name = models.CharField(max_length=50)

#     @property
#     def leader(self):
#         """get the leader of the department"""
#         return self.staff.objects.get(is_leader=True).name

# class Staffship(models.Model):
#     """staffship"""
#     staff = models.ForeignKey(MyUser)
#     department = models.ForeignKey(Department)

#     @property
#     def position(self):
#         """return the position of the user in the ship"""
#         return self.staff.position

