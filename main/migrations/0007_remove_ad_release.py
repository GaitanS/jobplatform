# Generated by Django 4.0.3 on 2022-04-02 18:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_ad_location'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ad',
            name='release',
        ),
    ]