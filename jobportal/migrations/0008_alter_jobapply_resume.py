# Generated by Django 3.2.5 on 2022-01-19 23:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobportal', '0007_alter_jobapply_resume'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobapply',
            name='resume',
            field=models.FileField(default='', upload_to='image'),
            preserve_default=False,
        ),
    ]
