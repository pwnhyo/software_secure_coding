# Generated by Django 3.2.5 on 2021-08-23 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_name', models.CharField(max_length=6)),
                ('user_id', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('user_pw', models.CharField(max_length=15)),
                ('user_email', models.EmailField(max_length=254)),
                ('user_phonenumber', models.CharField(max_length=15)),
                ('user_level', models.IntegerField()),
            ],
        ),
    ]
