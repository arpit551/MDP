# Generated by Django 2.1.1 on 2018-10-24 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0011_auto_20181023_1013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='depart',
            field=models.DateField(blank=True, null=True),
        ),
    ]
