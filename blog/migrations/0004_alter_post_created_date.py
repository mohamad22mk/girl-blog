# Generated by Django 4.1.2 on 2022-10-28 02:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_post_created_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 28, 2, 50, 2, 544727, tzinfo=datetime.timezone.utc)),
        ),
    ]
