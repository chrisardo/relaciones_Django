# Generated by Django 4.2.5 on 2023-09-30 01:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manytoone', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reporter',
            old_name='frist_name',
            new_name='first_name',
        ),
    ]
