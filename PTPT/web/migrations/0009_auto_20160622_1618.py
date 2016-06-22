# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-22 08:18
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0008_auto_20160622_1527'),
    ]

    operations = [
        migrations.CreateModel(
            name='schedule_choices',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('schedule_choice', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='tuition_type_choices',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tuition_choice', models.CharField(max_length=20)),
            ],
        ),
        migrations.AlterField(
            model_name='tutor',
            name='faculty',
            field=models.CharField(choices=[('arts and social sciences', 'Arts and Social Sciences'), ('computing', 'Computing'), ('science', 'Science'), ('business', 'Business'), ('dentistry', 'Dentistry'), ('design & environment', 'Design & Environment'), ('duke-nus', 'Duke-NUS'), ('engineering', 'Engineering'), ('law', 'Law'), ('medicine', 'Medicine'), ('music', 'Music'), ('yale-nus', 'Yale-NUS')], default='', max_length=30),
        ),
        migrations.RemoveField(
            model_name='tutor',
            name='preferred_schedule',
        ),
        migrations.RemoveField(
            model_name='tutor',
            name='preferred_tuition_type',
        ),
        migrations.AlterField(
            model_name='tutor',
            name='user',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, unique=True, verbose_name='user'),
        ),
        migrations.AlterField(
            model_name='tutor',
            name='year_of_study',
            field=models.CharField(choices=[('year 1', 'Year 1'), ('year 2', 'Year 2'), ('year 3', 'Year 3'), ('year 4', 'Year 4')], default='', max_length=10),
        ),
        migrations.AddField(
            model_name='tutor',
            name='preferred_schedule',
            field=models.ManyToManyField(to='web.schedule_choices'),
        ),
        migrations.AddField(
            model_name='tutor',
            name='preferred_tuition_type',
            field=models.ManyToManyField(to='web.tuition_type_choices'),
        ),
    ]
