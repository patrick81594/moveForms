# Generated by Django 2.1 on 2018-08-29 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mvForms', '0021_auto_20180829_1154'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='username',
            field=models.CharField(default='none', max_length=100),
        ),
    ]