# Generated by Django 5.0.6 on 2024-11-25 16:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('dob', models.DateField()),
                ('nid', models.CharField(max_length=20)),
                ('present_address', models.TextField()),
                ('permanent_address', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='owner_images/')),
                ('phone_number', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
                ('licence_number', models.CharField(max_length=20, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Fine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('violation_type', models.CharField(max_length=100)),
                ('violation_time', models.DateTimeField()),
                ('violation_location', models.CharField(max_length=100)),
                ('licence_number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fines', to='traffic.owner')),
            ],
        ),
        migrations.CreateModel(
            name='Expiry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('expiry_date', models.DateField()),
                ('licence_number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='expiry', to='traffic.owner')),
            ],
        ),
    ]
