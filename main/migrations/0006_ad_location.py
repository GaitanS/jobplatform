# Generated by Django 4.0.3 on 2022-04-02 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_ad'),
    ]

    operations = [
        migrations.AddField(
            model_name='ad',
            name='location',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
