# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Staffuser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, null=True, verbose_name='\u59d3\u540d')),
                ('mobile', models.CharField(max_length=50, null=True, verbose_name='\u624b\u673a')),
                ('create_at', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('staff_type', models.CharField(max_length=100, verbose_name='\u4eba\u5458\u8eab\u4efd', choices=[(b'teacher', '\u6559\u5e08'), (b'student', '\u5b66\u751f')])),
                ('department', models.CharField(max_length=100, verbose_name='\u6240\u5728\u90e8\u95e8', choices=[(b'C', '\u90e8\u95e8C'), (b'B', '\u90e8\u95e8B'), (b'A', '\u90e8\u95e8A')])),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
