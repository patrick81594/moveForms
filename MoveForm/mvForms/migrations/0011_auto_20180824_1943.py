# Generated by Django 2.1 on 2018-08-24 23:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mvForms', '0010_moveform_publication_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='moveform',
            name='publication_date',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
