# Generated by Django 3.2.9 on 2021-11-06 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0012_auto_20211105_1245'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterModelOptions(
            name='actor',
            options={'ordering': ('id',), 'verbose_name': 'Cast', 'verbose_name_plural': 'Casts'},
        ),
        migrations.AlterField(
            model_name='actor',
            name='profile_image',
            field=models.ImageField(upload_to='movie/actor/images'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='poster',
            field=models.ImageField(upload_to='movie/movie/images'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='video',
            field=models.FileField(upload_to='movie/movie/videos'),
        ),
    ]
