# Generated by Django 4.2.3 on 2023-08-11 10:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_advertisements', '0004_advertisement_img'),
    ]

    operations = [
        migrations.RenameField(
            model_name='advertisement',
            old_name='img',
            new_name='image',
        ),
    ]