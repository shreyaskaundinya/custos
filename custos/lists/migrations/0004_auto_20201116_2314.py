# Generated by Django 3.1.3 on 2020-11-16 23:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0003_auto_20201116_2243'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='expected_elapsed_timestamp',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
