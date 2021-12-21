# Generated by Django 3.2.9 on 2021-12-21 04:44

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0003_auto_20211211_0313'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='age',
            new_name='is_above_18',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='mobileNo',
            new_name='mobile_no',
        ),
        migrations.AddField(
            model_name='user',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='user_name',
            field=models.CharField(default='', max_length=10, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]
