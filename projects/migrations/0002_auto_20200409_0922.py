# Generated by Django 3.0.4 on 2020-04-09 09:22

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=django.core.files.storage.FileSystemStorage(location='/media/photos')),
        ),
    ]
