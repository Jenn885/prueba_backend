# Generated by Django 4.0.4 on 2022-04-26 02:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Jobs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gender',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('birth_date', models.DateField(null=True)),
                ('gender_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='employees.gender')),
                ('job_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Jobs.job')),
            ],
        ),
    ]