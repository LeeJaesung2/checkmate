# Generated by Django 3.2.5 on 2021-07-27 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0002_auto_20210727_0723'),
    ]

    operations = [
        migrations.AlterField(
            model_name='surveyoptional',
            name='mbti',
            field=models.CharField(blank=True, max_length=4, null=True),
        ),
    ]
