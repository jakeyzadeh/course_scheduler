# Generated by Django 2.1.4 on 2018-12-08 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course_sched', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('crn', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('building', models.CharField(max_length=50)),
                ('number', models.IntegerField(default=0)),
            ],
        ),
        migrations.DeleteModel(
            name='Courses',
        ),
    ]
