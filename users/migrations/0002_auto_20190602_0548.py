# Generated by Django 2.2.1 on 2019-06-02 05:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='biograbphy',
            new_name='biography',
        ),
    ]