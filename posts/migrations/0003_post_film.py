# Generated by Django 2.1 on 2022-03-14 06:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0003_auto_20220314_0655'),
        ('posts', '0002_post_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='film',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='movies.Movie'),
        ),
    ]
