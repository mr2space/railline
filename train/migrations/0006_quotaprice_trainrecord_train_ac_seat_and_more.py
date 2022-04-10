# Generated by Django 4.0.1 on 2022-04-10 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('train', '0005_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='quotaPrice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('general', models.FloatField()),
                ('sleeper', models.FloatField()),
                ('Ac', models.FloatField()),
                ('Seat', models.FloatField()),
            ],
        ),
        migrations.AddField(
            model_name='trainrecord',
            name='train_ac_seat',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='trainrecord',
            name='train_general_seat',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='trainrecord',
            name='train_seat_seat',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='trainrecord',
            name='train_sleeper_seat',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='trainrecord',
            name='train_start_date',
            field=models.DateField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='trainrecord',
            name='train_total_seat',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='trainroutetime',
            name='train_time_1',
            field=models.TimeField(),
        ),
        migrations.AlterField(
            model_name='trainroutetime',
            name='train_time_2',
            field=models.TimeField(),
        ),
        migrations.AlterField(
            model_name='trainroutetime',
            name='train_time_3',
            field=models.TimeField(),
        ),
        migrations.AlterField(
            model_name='trainroutetime',
            name='train_time_4',
            field=models.TimeField(),
        ),
        migrations.AlterField(
            model_name='trainroutetime',
            name='train_time_5',
            field=models.TimeField(),
        ),
        migrations.AlterField(
            model_name='trainroutetime',
            name='train_time_destination',
            field=models.TimeField(),
        ),
        migrations.AlterField(
            model_name='trainroutetime',
            name='train_time_starting',
            field=models.TimeField(),
        ),
    ]