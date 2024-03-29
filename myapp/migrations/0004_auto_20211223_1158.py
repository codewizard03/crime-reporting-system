# Generated by Django 3.2.10 on 2021-12-23 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_remove_user_details_kcno'),
    ]

    operations = [
        migrations.CreateModel(
            name='district_master',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state_id', models.IntegerField()),
                ('district_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('msg', models.CharField(max_length=500)),
                ('dt', models.CharField(max_length=50)),
                ('tm', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='look_out_master',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('station_id', models.IntegerField()),
                ('name', models.CharField(max_length=50)),
                ('remarks', models.CharField(max_length=500)),
                ('pic', models.CharField(max_length=500)),
                ('dt', models.CharField(max_length=50)),
                ('tm', models.CharField(max_length=50)),
                ('status', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='message_master',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user1_id', models.IntegerField()),
                ('user2_id', models.IntegerField()),
                ('msg', models.CharField(max_length=500)),
                ('dt', models.CharField(max_length=50)),
                ('tm', models.CharField(max_length=50)),
                ('status', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='place_master',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('district_id', models.IntegerField()),
                ('place_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='police_station_master',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('station_name', models.CharField(max_length=500)),
                ('station_type', models.CharField(max_length=500)),
                ('station_descp', models.CharField(max_length=500)),
                ('saddr', models.CharField(max_length=500)),
                ('spin', models.CharField(max_length=50)),
                ('place_id', models.IntegerField()),
                ('s_contact1', models.CharField(max_length=20)),
                ('s_contact2', models.CharField(max_length=20)),
                ('s_email', models.CharField(max_length=500)),
                ('status', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='report_pics',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('report_id', models.IntegerField()),
                ('pic_path', models.CharField(max_length=150)),
                ('pic_info', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='state_master',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='station_user',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('police_station_id', models.IntegerField()),
                ('user_id', models.IntegerField()),
                ('name', models.CharField(max_length=50)),
                ('designation', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=500)),
                ('contact', models.CharField(max_length=20)),
                ('dt', models.CharField(max_length=50)),
                ('tm', models.CharField(max_length=50)),
                ('status', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='user_report_followups',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('report_id', models.IntegerField()),
                ('user_id', models.IntegerField()),
                ('remarks', models.CharField(max_length=500)),
                ('dt', models.CharField(max_length=50)),
                ('tm', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='user_report_master',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('station_id', models.IntegerField()),
                ('type_id', models.IntegerField()),
                ('descrption', models.CharField(max_length=500)),
                ('addr', models.CharField(max_length=500)),
                ('place_id', models.IntegerField()),
                ('dt', models.CharField(max_length=50)),
                ('tm', models.CharField(max_length=50)),
                ('status', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='user_details',
            name='aadhaar_no',
            field=models.CharField(default='', max_length=25),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user_details',
            name='age',
            field=models.CharField(max_length=25),
        ),
        migrations.AlterField(
            model_name='user_details',
            name='contact',
            field=models.CharField(max_length=25),
        ),
        migrations.AlterField(
            model_name='user_details',
            name='pin',
            field=models.CharField(max_length=25),
        ),
    ]
