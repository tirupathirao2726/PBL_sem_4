# Generated by Django 3.2 on 2021-07-15 02:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='upload',
            name='uploaded_file',
            field=models.FileField(upload_to='csv_files/'),
        ),
    ]
