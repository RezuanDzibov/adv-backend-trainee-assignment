# Generated by Django 4.0.3 on 2022-03-17 11:34

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('ad_wall', '0002_image_headline'),
    ]

    operations = [
        migrations.AddField(
            model_name='ad',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
