# Generated by Django 4.2.4 on 2024-03-22 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('history', '0003_booking_remove_history_user_delete_buying_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='total_cost',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]