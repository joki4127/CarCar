# Generated by Django 4.0.3 on 2022-10-26 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service_rest', '0010_alter_serviceappointment_automobile_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='serviceappointment',
            name='time',
            field=models.TimeField(null=True),
        ),
    ]
