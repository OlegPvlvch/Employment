# Generated by Django 2.2.7 on 2019-12-10 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0006_auto_20191210_1908'),
    ]

    operations = [
        migrations.AlterField(
            model_name='worktime',
            name='date_end',
            field=models.DateTimeField(),
        ),
    ]
