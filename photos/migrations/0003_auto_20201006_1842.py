# Generated by Django 3.1.2 on 2020-10-06 15:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0002_auto_20201006_1826'),
    ]

    operations = [
        migrations.RenameField(
            model_name='image',
            old_name='Image_image',
            new_name='Image',
        ),
    ]
