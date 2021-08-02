# Generated by Django 3.2.5 on 2021-08-02 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='surveyoptional',
            name='bug',
            field=models.CharField(choices=[('0', '선택안함'), ('1', '잘잡음'), ('2', '못잡음')], default='0', max_length=1),
        ),
        migrations.AlterField(
            model_name='surveyoptional',
            name='game',
            field=models.CharField(blank=True, choices=[('0', '선택안함'), ('1', '자주'), ('2', '가끔'), ('3', '안함')], max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='surveyoptional',
            name='keyboard',
            field=models.CharField(blank=True, choices=[('0', '선택안함'), ('1', '타이핑&게임 자주함'), ('2', '거의 안함')], max_length=1, null=True),
        ),
    ]
