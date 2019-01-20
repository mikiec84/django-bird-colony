# Generated by Django 2.1.5 on 2019-01-19 21:03

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('birds', '0004_auto_20180322_1729'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='event',
            options={'get_latest_by': 'date', 'ordering': ['-date']},
        ),
        migrations.RemoveField(
            model_name='status',
            name='category',
        ),
        migrations.AddField(
            model_name='animal',
            name='attributes',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, default=dict, help_text='specify additional attributes for the animal'),
        ),
    ]