# Generated by Django 3.2.5 on 2021-08-24 03:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_rename_address_finishtime_address_address_usetime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='Address_usetime',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
