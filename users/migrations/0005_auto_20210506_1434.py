# Generated by Django 3.1.3 on 2021-05-06 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_profile_company'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='company',
        ),
        migrations.AddField(
            model_name='user',
            name='company',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='company'),
        ),
    ]