# Generated by Django 4.1.3 on 2022-11-25 16:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='doctor',
            old_name='price',
            new_name='consultation_fee',
        ),
    ]
