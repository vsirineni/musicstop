# Generated by Django 2.2.5 on 2020-04-29 23:44

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('courseapp', '0001_initial'),
        ('batchapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=50)),
                ('phone', models.IntegerField(unique=True)),
                ('email', models.EmailField(max_length=50, unique=True)),
                ('date', models.DateField(default=datetime.datetime.now)),
                ('select_batch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='batchapp.Batch')),
                ('select_course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courseapp.CourseModel')),
            ],
        ),
    ]