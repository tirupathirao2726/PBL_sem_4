# Generated by Django 3.2 on 2021-07-15 10:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0004_createddatabases_count'),
    ]

    operations = [
        migrations.RenameField(
            model_name='createddatabases',
            old_name='count',
            new_name='no_of_branches',
        ),
    ]