# Generated by Django 2.2.5 on 2022-11-12 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0009_auto_20221108_1212'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='guests',
            field=models.IntegerField(help_text='How many people are staying?'),
        ),
    ]
