# Generated by Django 2.2.3 on 2019-07-20 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0004_auto_20190719_0213'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='user_dob',
            field=models.DateTimeField(),
        ),
    ]
