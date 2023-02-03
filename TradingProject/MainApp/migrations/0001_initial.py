# Generated by Django 4.0.4 on 2023-02-03 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Candle',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('open', models.FloatField()),
                ('high', models.FloatField()),
                ('low', models.FloatField()),
                ('close', models.FloatField()),
                ('date', models.DateTimeField()),
            ],
        ),
    ]