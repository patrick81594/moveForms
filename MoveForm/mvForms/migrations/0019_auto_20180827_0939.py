# Generated by Django 2.1 on 2018-08-27 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mvForms', '0018_auto_20180826_1927'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='password',
            field=models.CharField(default='password', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='userName',
            field=models.CharField(default='User Name', max_length=100),
            preserve_default=False,
        ),
    ]
