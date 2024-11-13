# Generated by Django 5.1.3 on 2024-11-12 12:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_name', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=2000)),
                ('hosted_by', models.CharField(max_length=200)),
                ('datetime', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Attendees',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('semester', models.CharField(max_length=10)),
                ('event_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='event_management.events')),
            ],
        ),
    ]