# Generated by Django 3.1.5 on 2021-03-23 22:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('target', '0027_auto_20210323_2212'),
    ]

    operations = [
        migrations.AddField(
            model_name='attack',
            name='respect',
            field=models.FloatField(default=0.0),
        ),
    ]