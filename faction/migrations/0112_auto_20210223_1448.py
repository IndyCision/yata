# Generated by Django 3.1.5 on 2021-02-23 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('faction', '0111_auto_20210222_2034'),
    ]

    operations = [
        migrations.AddField(
            model_name='revive',
            name='chance',
            field=models.IntegerField(default=100),
        ),
        migrations.AddField(
            model_name='revive',
            name='result',
            field=models.BooleanField(default=True),
        ),
    ]