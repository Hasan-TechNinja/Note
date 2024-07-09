# Generated by Django 5.0.6 on 2024-07-07 16:49

import tinymce.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('content', tinymce.models.HTMLField()),
                ('create_date', models.DateField()),
                ('update_date', models.DateField()),
            ],
        ),
    ]
