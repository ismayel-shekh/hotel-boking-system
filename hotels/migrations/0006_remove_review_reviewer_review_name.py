# Generated by Django 4.2.4 on 2024-04-01 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotels', '0005_alter_hotel_avilable_room'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='reviewer',
        ),
        migrations.AddField(
            model_name='review',
            name='name',
            field=models.CharField(default=0, max_length=250),
            preserve_default=False,
        ),
    ]
