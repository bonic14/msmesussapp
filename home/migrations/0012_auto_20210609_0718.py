# Generated by Django 3.1.1 on 2021-06-09 07:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_remove_msmes_sector'),
    ]

    operations = [
        migrations.RenameField(
            model_name='msmes',
            old_name='category',
            new_name='sector',
        ),
    ]
