# Generated by Django 4.1.1 on 2022-12-08 09:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0002_alter_hotel_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now_add=True)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('booking_type', models.CharField(choices=[('Pre Paid', 'Pre Paid'), ('Post Paid', 'Post Paid')], max_length=100)),
                ('hotel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.hotel')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.DeleteModel(
            name='HotelBooking',
        ),
    ]
