# Generated by Django 2.1b1 on 2018-08-02 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ronaldo', '0004_links_the_link'),
    ]

    operations = [
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('match_description', models.CharField(max_length=200)),
                ('match_details', models.CharField(max_length=1000)),
                ('match_logo', models.FileField(upload_to='')),
            ],
        ),
    ]
