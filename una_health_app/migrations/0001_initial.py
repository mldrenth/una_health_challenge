# Generated by Django 4.0.3 on 2022-03-18 08:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='GlucoseValue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('device', models.CharField(max_length=255)),
                ('serial_number', models.CharField(max_length=255)),
                ('time_stamp', models.DateTimeField()),
                ('recording_type', models.IntegerField()),
                ('glucose_history', models.IntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='una_health_app.user')),
            ],
        ),
    ]