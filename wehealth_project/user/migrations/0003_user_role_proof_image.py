# Generated by Django 4.1.3 on 2022-11-24 22:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_user_is_registered_alter_user_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='role_proof_image',
            field=models.ImageField(default=1, upload_to=''),
            preserve_default=False,
        ),
    ]
