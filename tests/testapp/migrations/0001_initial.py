# Generated by Django 2.2.10 on 2020-05-09 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ModelA',
            fields=[
                ('auto', models.AutoField(primary_key=True, serialize=False)),
                ('char', models.CharField(max_length=24)),
                ('boolean', models.BooleanField()),
                ('nullboolean', models.NullBooleanField()),
                ('date', models.DateField()),
                ('datetime', models.DateTimeField()),
                ('time', models.TimeField()),
                ('duration', models.DurationField()),
                ('integer', models.IntegerField()),
                ('float', models.FloatField()),
                ('decimal', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
