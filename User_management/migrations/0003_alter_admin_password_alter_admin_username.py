# Generated by Django 4.1.5 on 2023-02-24 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User_management', '0002_admin_alter_userregistration_address_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admin',
            name='password',
            field=models.CharField(max_length=20, verbose_name='Password'),
        ),
        migrations.AlterField(
            model_name='admin',
            name='username',
            field=models.CharField(max_length=20, verbose_name='UserName'),
        ),
    ]
