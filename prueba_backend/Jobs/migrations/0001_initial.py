# Generated by Django 4.0.4 on 2022-04-26 02:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('salary', models.DecimalField(decimal_places=2, max_digits=9)),
            ],
        ),
    ]
