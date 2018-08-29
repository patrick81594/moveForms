# Generated by Django 2.1 on 2018-08-29 18:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mvForms', '0022_user_username'),
    ]

    operations = [
        migrations.CreateModel(
            name='assignedTask',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assignee', models.CharField(max_length=200)),
                ('task', models.CharField(max_length=200)),
                ('dateDue', models.DateTimeField()),
                ('dateAssigned', models.DateTimeField(auto_now_add=True)),
                ('relation', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='mvForms.moveForm')),
            ],
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(default='', max_length=100),
        ),
    ]
