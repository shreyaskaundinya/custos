# Generated by Django 3.1.3 on 2020-11-16 17:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_privilege'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Privilege',
        ),
    ]