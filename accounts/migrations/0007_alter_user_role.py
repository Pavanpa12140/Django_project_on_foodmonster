# Generated by Django 4.1.2 on 2022-11-24 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_alter_user_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.PositiveSmallIntegerField(choices=[('Restaurant', 'Restaurant'), ('Customer', 'Customer')]),
        ),
    ]