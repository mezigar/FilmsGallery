# Generated by Django 2.1 on 2022-03-14 06:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_auto_20220313_1239'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='movie',
            options={'ordering': ['title']},
        ),
    ]
