# Generated by Django 2.1.5 on 2019-01-23 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20190123_1129'),
    ]

    operations = [
        migrations.AlterField(
            model_name='relationship',
            name='is_deleted',
            field=models.BooleanField(default=False, verbose_name='已刪除'),
        ),
    ]
