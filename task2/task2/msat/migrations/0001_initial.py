# Generated by Django 3.0.6 on 2020-05-18 03:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MSAT',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('r_id', models.IntegerField()),
                ('stud_id', models.CharField(max_length=50)),
                ('response', models.CharField(max_length=30)),
                ('timestamp', models.DurationField()),
                ('mark_scored', models.IntegerField()),
                ('answered', models.CharField(max_length=10)),
            ],
        ),
    ]
