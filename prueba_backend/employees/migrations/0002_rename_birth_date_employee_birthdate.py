# Generated by Django 4.0.4 on 2022-04-26 02:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='birth_date',
            new_name='birthdate',
        ),
    ]
