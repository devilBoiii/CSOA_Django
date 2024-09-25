# Generated by Django 5.0.6 on 2024-07-03 06:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cso_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='MBO_list',
            new_name='FCSO_lists',
        ),
        migrations.RenameModel(
            old_name='FCSO_list',
            new_name='MBO_lists',
        ),
        migrations.RenameModel(
            old_name='PBO_list',
            new_name='PBO_lists',
        ),
        migrations.RenameField(
            model_name='fcso_lists',
            old_name='mbo_cso_contact',
            new_name='fcso_cso_contact',
        ),
        migrations.RenameField(
            model_name='fcso_lists',
            old_name='mbo_cso_email',
            new_name='fcso_cso_email',
        ),
        migrations.RenameField(
            model_name='fcso_lists',
            old_name='mbo_cso_focal',
            new_name='fcso_cso_focal',
        ),
        migrations.RenameField(
            model_name='fcso_lists',
            old_name='mbo_cso_id',
            new_name='fcso_cso_id',
        ),
        migrations.RenameField(
            model_name='fcso_lists',
            old_name='mbo_cso_link',
            new_name='fcso_cso_link',
        ),
        migrations.RenameField(
            model_name='fcso_lists',
            old_name='mbo_cso_logo',
            new_name='fcso_cso_logo',
        ),
        migrations.RenameField(
            model_name='fcso_lists',
            old_name='mbo_cso_name',
            new_name='fcso_cso_name',
        ),
        migrations.RenameField(
            model_name='fcso_lists',
            old_name='mbo_cso_registered',
            new_name='fcso_cso_registered',
        ),
        migrations.RenameField(
            model_name='fcso_lists',
            old_name='mbo_cso_url',
            new_name='fcso_cso_url',
        ),
        migrations.RenameField(
            model_name='fcso_lists',
            old_name='mbo_cso_validy',
            new_name='fcso_cso_validy',
        ),
        migrations.RenameField(
            model_name='mbo_lists',
            old_name='fcso_cso_contact',
            new_name='mbo_cso_contact',
        ),
        migrations.RenameField(
            model_name='mbo_lists',
            old_name='fcso_cso_email',
            new_name='mbo_cso_email',
        ),
        migrations.RenameField(
            model_name='mbo_lists',
            old_name='fcso_cso_focal',
            new_name='mbo_cso_focal',
        ),
        migrations.RenameField(
            model_name='mbo_lists',
            old_name='fcso_cso_id',
            new_name='mbo_cso_id',
        ),
        migrations.RenameField(
            model_name='mbo_lists',
            old_name='fcso_cso_link',
            new_name='mbo_cso_link',
        ),
        migrations.RenameField(
            model_name='mbo_lists',
            old_name='fcso_cso_logo',
            new_name='mbo_cso_logo',
        ),
        migrations.RenameField(
            model_name='mbo_lists',
            old_name='fcso_cso_name',
            new_name='mbo_cso_name',
        ),
        migrations.RenameField(
            model_name='mbo_lists',
            old_name='fcso_cso_registered',
            new_name='mbo_cso_registered',
        ),
        migrations.RenameField(
            model_name='mbo_lists',
            old_name='fcso_cso_url',
            new_name='mbo_cso_url',
        ),
        migrations.RenameField(
            model_name='mbo_lists',
            old_name='fcso_cso_validy',
            new_name='mbo_cso_validy',
        ),
    ]