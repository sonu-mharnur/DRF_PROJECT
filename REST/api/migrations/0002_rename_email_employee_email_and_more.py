# Generated by Django 4.1.6 on 2023-12-14 10:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='Email',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='employee',
            old_name='Name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='employee',
            old_name='Password',
            new_name='password',
        ),
        migrations.RenameField(
            model_name='employee',
            old_name='Phone',
            new_name='phone',
        ),
    ]