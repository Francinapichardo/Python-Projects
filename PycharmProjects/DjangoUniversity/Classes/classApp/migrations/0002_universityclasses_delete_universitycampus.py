# Generated by Django 4.1.3 on 2022-11-17 02:53

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('classApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UniversityClasses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, default='', max_length=60)),
                ('course_number', models.IntegerField(blank=True, default='')),
                ('instructor_name', models.CharField(blank=True, default='', max_length=60, null=None)),
            ],
            options={
                'verbose_name_plural': 'University Classes',
            },
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
        migrations.DeleteModel(
            name='UniversityCampus',
        ),
    ]