# Generated by Django 3.2.5 on 2022-01-20 05:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobportal', '0011_job_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='category',
        ),
        migrations.DeleteModel(
            name='InnerCategory',
        ),
    ]
