# Generated by Django 5.0.1 on 2025-02-08 01:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='label',
            name='file_type',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
