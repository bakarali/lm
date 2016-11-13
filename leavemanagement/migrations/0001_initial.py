# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-11-11 13:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=200)),
                ('dob', models.DateField()),
                ('joining_date', models.DateField()),
                ('role', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Employee_Relation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Employee_id', models.IntegerField()),
                ('Manager_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Leave',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Emp_id', models.IntegerField()),
                ('leave_type_id', models.IntegerField()),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('status', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Leave_type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=200)),
                ('max_days', models.IntegerField()),
            ],
        ),
    ]
