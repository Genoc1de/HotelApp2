# Generated by Django 4.1.4 on 2022-12-09 04:37

from django.db import migrations
import phone_field.models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_booking_delete_hotelbooking'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='booking_type',
        ),
        migrations.AddField(
            model_name='booking',
            name='phone',
            field=phone_field.models.PhoneField(blank=True, help_text='Contact phone number', max_length=31),
        ),
    ]
