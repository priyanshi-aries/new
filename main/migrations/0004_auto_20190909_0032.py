# Generated by Django 2.2.4 on 2019-09-08 19:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20190124_1800'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutorial',
            name='tutorial_published',
            field=models.DateTimeField(default=datetime.datetime(2019, 9, 9, 0, 31, 59, 554846), verbose_name='date published'),
        ),
    ]
