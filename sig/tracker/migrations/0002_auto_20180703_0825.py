# Generated by Django 2.0 on 2018-07-03 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sig',
            name='sig_name',
            field=models.CharField(max_length=100),
        ),
    ]
