# Generated by Django 3.2.5 on 2021-08-23 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='Address_finished',
            field=models.CharField(default=0, max_length=5),
        ),
    ]