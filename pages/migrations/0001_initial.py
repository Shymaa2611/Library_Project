# Generated by Django 4.2.1 on 2023-05-18 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='doctor_Data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doctor_name', models.CharField(max_length=100)),
                ('doctor_subTitle', models.CharField(max_length=100)),
                ('Specialist_doctor', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('address_detai', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=3)),
                ('Waiting_time', models.TimeField()),
                ('working_hours', models.TimeField()),
                ('number_phone', models.CharField(max_length=12)),
            ],
        ),
    ]
