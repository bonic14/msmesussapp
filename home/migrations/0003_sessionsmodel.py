# Generated by Django 3.1.1 on 2021-04-01 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_registration'),
    ]

    operations = [
        migrations.CreateModel(
            name='SessionsModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sessionID', models.CharField(max_length=255)),
                ('newsession', models.CharField(max_length=255)),
            ],
        ),
    ]
