# Generated by Django 2.1 on 2018-08-24 23:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mvForms', '0012_auto_20180824_1947'),
    ]

    operations = [
        migrations.AlterField(
            model_name='moveform',
            name='publication_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]