# Generated by Django 4.1.13 on 2023-12-17 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mailing', '0008_remove_mailinglog_id_mailing'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mailinglog',
            name='client',
        ),
        migrations.AlterField(
            model_name='mailinglog',
            name='status',
            field=models.CharField(choices=[('1', 'Успешно'), ('0', 'Неуспешно')], max_length=20, verbose_name='статус попытки'),
        ),
        migrations.AddField(
            model_name='mailinglog',
            name='client',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='клиент'),
        ),
    ]
