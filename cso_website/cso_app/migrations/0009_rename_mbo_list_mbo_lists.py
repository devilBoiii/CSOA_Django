# Generated by Django 5.0.6 on 2024-07-03 08:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cso_app', '0008_rename_mbo_lists_mbo_list'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='MBO_list',
            new_name='MBO_lists',
        ),
    ]