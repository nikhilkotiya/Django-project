# Generated by Django 3.1.3 on 2021-05-07 07:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('test_api', '0005_auto_20210507_1122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quize',
            name='test_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='test_api.test_name'),
        ),
    ]
