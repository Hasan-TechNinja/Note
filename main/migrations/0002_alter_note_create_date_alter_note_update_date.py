# Generated by Django 5.0.6 on 2024-07-08 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='create_date',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='note',
            name='update_date',
            field=models.DateField(blank=True),
        ),
    ]