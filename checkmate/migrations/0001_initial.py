
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Offcampus_Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('content', models.TextField()),
                ('pub_date', models.DateTimeField(auto_now=True)),
                ('image', models.ImageField(blank=True, upload_to='offcampus_image/%Y/%m/%d')),
                ('preface', models.CharField(choices=[('해결했어요', '해결했어요'), ('질문있어요', '질문있어요'), ('원룸정보', '원룸정보')], max_length=10)),
                ('preface_2', models.CharField(choices=[('생활정보', '생활정보'), ('원룸', '원룸')], max_length=10)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Domitory_Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('content', models.TextField()),
                ('pub_date', models.DateTimeField(auto_now=True)),
                ('image', models.ImageField(blank=True, upload_to='domitory_image/%Y/%m/%d')),
                ('preface', models.CharField(choices=[('해결했어요', '해결했어요'), ('질문있어요', '질문있어요'), ('기숙사정보', '기숙사정보'), ('기숙사후기', '기숙사후기')], max_length=10)),
                ('preface_2', models.CharField(choices=[('생활정보', '생활정보'), ('아람관', '아람관')], max_length=10)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
