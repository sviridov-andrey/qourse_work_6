# Generated by Django 4.1.13 on 2023-12-11 17:50

import datetime
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
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='электронная почта')),
                ('fio', models.CharField(max_length=100, verbose_name='ФИО')),
                ('comment', models.TextField(verbose_name='комментарий')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='пользователь')),
            ],
            options={
                'verbose_name': 'Клиент',
                'verbose_name_plural': 'Клиенты',
            },
        ),
        migrations.CreateModel(
            name='Mailing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='тема письма')),
                ('body', models.TextField(verbose_name='тело письма')),
                ('status', models.CharField(choices=[('created', 'создана'), ('running', 'запущена'), ('completed', 'завершена')], default='created', max_length=10, verbose_name='статус')),
                ('time_start', models.TimeField(help_text='Введите время в формате ЧЧ:ММ через знак :', verbose_name='начало времени отправки')),
                ('time_end', models.TimeField(help_text='Введите время в формате ЧЧ:ММ через знак :', verbose_name='окончание времени отправки')),
                ('periodicity', models.CharField(choices=[('day', 'раз в день'), ('week', 'раз в неделю'), ('mon', 'раз в месяц')], max_length=20, verbose_name='периодичность')),
                ('day', models.IntegerField(blank=True, help_text='Введите число при периодичности раз в месяц', null=True, verbose_name='день')),
                ('day_week', models.CharField(blank=True, choices=[('0', 'понедельник'), ('1', 'вторник'), ('2', 'среда'), ('3', 'четверг'), ('4', 'пятница'), ('5', 'суббота'), ('6', 'вскресенье')], help_text='Выберите день недели при периодичности раз в неделю', max_length=15, null=True, verbose_name='день недели')),
                ('is_active', models.BooleanField(default=True, verbose_name='активность рассылки')),
                ('clients', models.ManyToManyField(related_name='clients', to='mailing.client', verbose_name='клиенты')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='пользователь')),
            ],
            options={
                'verbose_name': 'письмо',
                'verbose_name_plural': 'письма',
            },
        ),
        migrations.CreateModel(
            name='MailingLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_try', models.DateTimeField(default=datetime.datetime.now, verbose_name='дата и время попытки')),
                ('status', models.IntegerField(choices=[(1, 'Успешно'), (0, 'Неуспешно')], verbose_name='статус попытки')),
                ('server_response', models.TextField(blank=True, null=True, verbose_name='ответ почтового сервера')),
                ('client', models.ManyToManyField(to='mailing.client', verbose_name='клиент')),
                ('mailing_list', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mailing.mailing', verbose_name='рассылка')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='пользователь')),
            ],
            options={
                'verbose_name': 'Лог',
                'verbose_name_plural': 'Логи',
            },
        ),
    ]
