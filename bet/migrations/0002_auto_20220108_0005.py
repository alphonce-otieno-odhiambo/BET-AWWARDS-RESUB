# Generated by Django 3.2.9 on 2022-01-07 21:05

import cloudinary.models
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('bet', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=200)),
                ('date_added', models.DateTimeField(default=django.utils.timezone.now)),
                ('image', cloudinary.models.CloudinaryField(max_length=255, verbose_name='image')),
            ],
        ),
        migrations.AddField(
            model_name='profile',
            name='profile_picture',
            field=cloudinary.models.CloudinaryField(default=django.utils.timezone.now, max_length=255, verbose_name='image'),
            preserve_default=False,
        ),
    ]
