# Generated by Django 2.1 on 2018-08-30 15:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mvForms', '0028_auto_20180830_0941'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='taskoverview',
            name='person',
        ),
        migrations.DeleteModel(
            name='taskOverview',
        ),
    ]
