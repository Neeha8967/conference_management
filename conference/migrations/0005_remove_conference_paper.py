# Generated by Django 2.2.13 on 2022-07-19 21:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('conference', '0004_conference_paper'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='conference',
            name='paper',
        ),
    ]