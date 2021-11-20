# Generated by Django 3.2.9 on 2021-11-05 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0010_auto_20211105_1140'),
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('profile_image', models.ImageField(upload_to='profile/images')),
            ],
        ),
    ]
