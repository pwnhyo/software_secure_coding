# Generated by Django 3.2.5 on 2021-08-24 03:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_rename_address_usedtime_address_address_finishtime'),
    ]

    operations = [
        migrations.RenameField(
            model_name='address',
            old_name='Address_finishtime',
            new_name='Address_usetime',
        ),
    ]