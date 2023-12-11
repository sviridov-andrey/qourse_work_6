# Generated by Django 4.1.13 on 2023-12-11 17:50

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
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='заголовок')),
                ('body', models.TextField(verbose_name='содержимое')),
                ('image', models.ImageField(blank=True, null=True, upload_to='', verbose_name='изображение')),
                ('date_of_creation', models.DateField(auto_now_add=True, verbose_name='Дата создания')),
                ('views_count', models.IntegerField(default=0, verbose_name='просмотры')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='пользователь')),
            ],
            options={
                'verbose_name': 'блог',
                'verbose_name_plural': 'блоги',
            },
        ),
    ]
