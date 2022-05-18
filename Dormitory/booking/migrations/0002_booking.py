# Generated by Django 4.0.4 on 2022-04-20 10:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booking.room')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booking.student')),
            ],
        ),
    ]