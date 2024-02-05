# Generated by Django 3.2.10 on 2021-12-27 04:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_auto_20211223_1158'),
    ]

    operations = [
        migrations.CreateModel(
            name='crime_type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='notice_board_master',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('station_id', models.IntegerField()),
                ('title', models.CharField(max_length=150)),
                ('pic_path', models.CharField(max_length=500)),
                ('descp', models.CharField(max_length=500)),
                ('dt', models.CharField(max_length=50)),
                ('tm', models.CharField(max_length=50)),
                ('status', models.CharField(max_length=50)),
            ],
        ),
    ]
