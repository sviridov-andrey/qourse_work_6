# Generated by Django 4.1.13 on 2023-12-12 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_user_ver_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='ver_code',
            field=models.CharField(default='669329587325', max_length=15, verbose_name='код из письма'),
        ),
    ]
