# Generated by Django 3.1.2 on 2020-10-11 02:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0002_auto_20201011_0534'),
    ]

    operations = [
        migrations.RenameField(
            model_name='image',
            old_name='image',
            new_name='Image',
        ),
    ]