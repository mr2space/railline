# Generated by Django 3.2.9 on 2022-01-02 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0009_auto_20211230_1610'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='useraddon_saving',
            name='otp',
        ),
        migrations.AlterField(
            model_name='useraddon_saving',
            name='address',
            field=models.CharField(default='', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='useraddon_saving',
            name='phone_no',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='usercreations',
            name='email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='usercreations',
            name='passwd',
            field=models.CharField(max_length=1800),
        ),
        migrations.AlterField(
            model_name='usercreations',
            name='phone_no',
            field=models.IntegerField(),
        ),
    ]