# Generated by Django 2.1 on 2018-08-24 23:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mvForms', '0009_remove_moveform_publication_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='moveform',
            name='publication_date',
            field=models.CharField(default=datetime.date(2018, 8, 24), max_length=50),
            preserve_default=False,
        ),
    ]
