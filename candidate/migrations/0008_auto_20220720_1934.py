# Generated by Django 2.2.13 on 2022-07-20 19:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('candidate', '0007_auto_20220720_1514'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='File',
            new_name='paper',
        ),
        migrations.RenameField(
            model_name='paper',
            old_name='paper',
            new_name='pdf',
        ),
    ]
