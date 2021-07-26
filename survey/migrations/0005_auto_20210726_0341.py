# Generated by Django 3.2.5 on 2021-07-26 03:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0004_auto_20210725_1403'),
    ]

    operations = [
        migrations.AlterField(
            model_name='surveyessential',
            name='bed_time',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='surveyessential',
            name='cleaning',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='surveyessential',
            name='earphone',
            field=models.NullBooleanField(),
        ),
        migrations.AlterField(
            model_name='surveyessential',
            name='invite_friends',
            field=models.NullBooleanField(),
        ),
        migrations.AlterField(
            model_name='surveyessential',
            name='smoke',
            field=models.NullBooleanField(),
        ),
        migrations.AlterField(
            model_name='surveyessential',
            name='wakeup_time',
            field=models.TimeField(blank=True, null=True),
        ),
    ]
