# Generated by Django 3.1.5 on 2021-04-14 14:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('acronym', models.CharField(db_index=True, default='-', max_length=8)),
                ('name', models.CharField(default='-', max_length=64)),
                ('tendancy_l_a', models.FloatField(default=0.0)),
                ('tendancy_l_b', models.FloatField(default=0.0)),
                ('tendancy_h_a', models.FloatField(default=0.0)),
                ('tendancy_h_b', models.FloatField(default=0.0)),
                ('tendancy_d_a', models.FloatField(default=0.0)),
                ('tendancy_d_b', models.FloatField(default=0.0)),
                ('tendancy_w_a', models.FloatField(default=0.0)),
                ('tendancy_w_b', models.FloatField(default=0.0)),
                ('tendancy_m_a', models.FloatField(default=0.0)),
                ('tendancy_m_b', models.FloatField(default=0.0)),
                ('tendancy_y_a', models.FloatField(default=0.0)),
                ('tendancy_y_b', models.FloatField(default=0.0)),
                ('timestamp', models.IntegerField(default=0)),
                ('current_price', models.FloatField(default=0.0)),
                ('current_price_previous', models.FloatField(default=0.0)),
                ('requirements', models.IntegerField(default=0)),
                ('description', models.CharField(default='-', max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.IntegerField(db_index=True, default=0)),
                ('current_price', models.FloatField(default=0.0)),
                ('stock', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stocks.stock')),
            ],
        ),
    ]