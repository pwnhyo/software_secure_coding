# Generated by Django 3.2.6 on 2021-08-26 23:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0021_address_address_storeid'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='Address_ridername',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
