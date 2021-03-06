# Generated by Django 4.0.3 on 2022-07-07 17:15

from django.db import migrations
from ..data import user_data, user_pass
from django.contrib.auth.hashers import make_password


class Migration(migrations.Migration):

    def new_user(apps, schema_editor):
        User = apps.get_model('base', 'User')

        def users_iterator():
            for indiv in user_data:
                yield User(**indiv, password = make_password(user_pass))
            
        User.objects.bulk_create(iter(users_iterator()))

    def remove_user(apps, schema_editor):
        User = apps.get_model('base', 'User')

        def user_email():
            for indiv in user_data:
                yield(indiv['email'])

        User.objects.filter(email__in = iter(user_email())).delete()
        

    dependencies = [
        ('base', '0009_alter_user_first_name_alter_user_last_name'),
    ]

    operations = [
        migrations.RunPython(new_user, remove_user)
    ]
