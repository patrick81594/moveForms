# Generated by Django 2.1 on 2018-08-30 16:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mvForms', '0029_auto_20180830_1145'),
    ]

    operations = [
        migrations.RenameField(
            model_name='assignedtask',
            old_name='relate',
            new_name='relatedForm',
        ),
    ]
