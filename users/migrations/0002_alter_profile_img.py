# Generated by Django 4.1 on 2022-08-14 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='img',
            field=models.ImageField(default='profilepic.png', upload_to='profile_pictures'),
        ),
    ]
