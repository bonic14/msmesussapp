# Generated by Django 3.1.1 on 2021-04-19 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_auto_20210408_1116'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ihuzo',
            name='email',
            field=models.CharField(default='', max_length=255),
        ),
    ]
