# Generated by Django 3.2.5 on 2021-08-24 04:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_alter_address_address_usetime'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='Address_checktime',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
