# Generated by Django 3.1.1 on 2020-09-26 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0008_remove_movie_total_audience'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='released_date',
            field=models.IntegerField(),
        ),
    ]