# Generated by Django 3.2.5 on 2021-08-24 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_alter_user_user_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_photo',
            field=models.ImageField(default='media/images/default_image.png', upload_to='images/'),
        ),
    ]