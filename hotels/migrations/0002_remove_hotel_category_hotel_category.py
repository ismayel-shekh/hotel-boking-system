# Generated by Django 4.2.4 on 2024-03-07 14:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hotels', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hotel',
            name='category',
        ),
        migrations.AddField(
            model_name='hotel',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='hotels.category'),
            preserve_default=False,
        ),
    ]
