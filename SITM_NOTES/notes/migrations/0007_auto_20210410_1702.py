# Generated by Django 3.1.4 on 2021-04-10 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0006_auto_20210410_1701'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notes',
            name='year',
        ),
        migrations.AddField(
            model_name='notes',
            name='branch',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AlterField(
            model_name='notes',
            name='subcode',
            field=models.CharField(default='', max_length=15),
        ),
    ]
