# Generated by Django 3.1.7 on 2021-08-19 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0037_auto_20210819_1923'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='name',
        ),
        migrations.AlterField(
            model_name='invoice',
            name='order_date',
            field=models.CharField(default='August 19, 202121:43:17', max_length=1000),
        ),
        migrations.AlterField(
            model_name='sellhistory',
            name='date',
            field=models.CharField(default='August 19, 202121:43:17', max_length=1000),
        ),
    ]
