# Generated by Django 4.2.4 on 2024-03-22 13:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('history', '0004_booking_total_cost'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='total_cost',
        ),
    ]