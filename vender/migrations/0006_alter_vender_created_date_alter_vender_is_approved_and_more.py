# Generated by Django 4.1.2 on 2022-11-16 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vender', '0005_alter_vender_vender_liciense'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vender',
            name='created_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='vender',
            name='is_approved',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='vender',
            name='modified_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]