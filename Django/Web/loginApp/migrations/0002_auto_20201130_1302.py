# Generated by Django 3.1.3 on 2020-11-30 04:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('loginApp', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Login',
            new_name='Signup',
        ),
        migrations.RenameField(
            model_name='signup',
            old_name='user_id',
            new_name='user_email',
        ),
    ]
