# Generated by Django 2.1b1 on 2018-07-24 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ronaldo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='links',
            name='details',
            field=models.CharField(default='', max_length=1000),
        ),
    ]
