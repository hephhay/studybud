# Generated by Django 4.0.6 on 2022-07-08 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0008_user_login_count'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(max_length=1, null=True),
        ),
    ]