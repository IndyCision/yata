# Generated by Django 3.1.5 on 2021-04-08 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('faction', '0130_spy_update'),
    ]

    operations = [
        migrations.AddField(
            model_name='spydatabase',
            name='update',
            field=models.IntegerField(default=0),
        ),
    ]