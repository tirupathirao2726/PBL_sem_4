# Generated by Django 3.2 on 2021-07-15 10:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0005_rename_count_createddatabases_no_of_branches'),
    ]

    operations = [
        migrations.RenameField(
            model_name='createddatabases',
            old_name='no_of_branches',
            new_name='no_of_branches_result_user_added',
        ),
    ]
