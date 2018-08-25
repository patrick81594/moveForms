# Generated by Django 2.1 on 2018-08-24 23:33

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('mvForms', '0007_remove_moveform_publication_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='moveform',
            name='publication_date',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]