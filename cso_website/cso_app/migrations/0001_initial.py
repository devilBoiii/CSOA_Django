# Generated by Django 5.0.6 on 2024-07-03 06:02

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='certificate_application',
            fields=[
                ('application_id', models.AutoField(primary_key=True, serialize=False)),
                ('application_date', models.DateTimeField(auto_now_add=True)),
                ('uploader_cso_name', models.CharField(blank=True, max_length=200, null=True)),
                ('status', models.CharField(blank=True, max_length=100, null=True)),
                ('certificate_application', models.FileField(upload_to='certificates/')),
            ],
        ),
        migrations.CreateModel(
            name='cso_closing_type',
            fields=[
                ('cso_closing_id', models.AutoField(primary_key=True, serialize=False)),
                ('cso_closing_type', models.CharField(blank=True, max_length=255, null=True)),
                ('cso_closing_description', models.CharField(blank=True, max_length=200, null=True)),
                ('status', models.CharField(blank=True, default='Active', max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='cso_types',
            fields=[
                ('cso_id', models.AutoField(primary_key=True, serialize=False)),
                ('cso_name', models.CharField(blank=True, max_length=255, null=True)),
                ('cso_prefix', models.CharField(blank=True, max_length=255, null=True)),
                ('cso_status', models.CharField(default='Active', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='dzongkhags',
            fields=[
                ('dzongkhag_id', models.AutoField(primary_key=True, serialize=False)),
                ('dzongkhag_name', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='FCSO_list',
            fields=[
                ('fcso_cso_id', models.AutoField(primary_key=True, serialize=False)),
                ('fcso_cso_name', models.CharField(blank=True, max_length=200, null=True)),
                ('fcso_cso_registered', models.DateTimeField(auto_now_add=True)),
                ('fcso_cso_validy', models.DateTimeField(blank=True, null=True)),
                ('fcso_cso_focal', models.CharField(blank=True, max_length=100, null=True)),
                ('fcso_cso_contact', models.CharField(blank=True, max_length=100)),
                ('fcso_cso_email', models.EmailField(blank=True, max_length=100, null=True)),
                ('fcso_cso_url', models.URLField(blank=True, null=True)),
                ('fcso_cso_link', models.CharField(blank=True, max_length=200, null=True)),
                ('fcso_cso_logo', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('status', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='gewog',
            fields=[
                ('gewog_id', models.AutoField(primary_key=True, serialize=False)),
                ('gewog_name', models.CharField(blank=True, max_length=255, null=True)),
                ('dzongkhag', models.CharField(blank=True, max_length=255, null=True)),
                ('status', models.CharField(blank=True, default='Active', max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='MBO_list',
            fields=[
                ('mbo_cso_id', models.AutoField(primary_key=True, serialize=False)),
                ('mbo_cso_name', models.CharField(blank=True, max_length=200, null=True)),
                ('mbo_cso_registered', models.DateTimeField(auto_now_add=True)),
                ('mbo_cso_validy', models.DateTimeField(blank=True, null=True)),
                ('mbo_cso_focal', models.CharField(blank=True, max_length=100, null=True)),
                ('mbo_cso_contact', models.CharField(blank=True, max_length=100)),
                ('mbo_cso_email', models.EmailField(blank=True, max_length=100, null=True)),
                ('mbo_cso_url', models.URLField(blank=True, null=True)),
                ('mbo_cso_link', models.CharField(blank=True, max_length=200, null=True)),
                ('mbo_cso_logo', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('status', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='organizations',
            fields=[
                ('organization_id', models.AutoField(primary_key=True, serialize=False)),
                ('organization_name', models.CharField(blank=True, max_length=220, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PBO_list',
            fields=[
                ('pbo_cso_id', models.AutoField(primary_key=True, serialize=False)),
                ('pbo_cso_name', models.CharField(blank=True, max_length=200, null=True)),
                ('pbo_cso_registered', models.DateTimeField(auto_now_add=True)),
                ('pbo_cso_vlidity', models.DateTimeField(blank=True, null=True)),
                ('pbo_cso_focal', models.CharField(blank=True, max_length=100, null=True)),
                ('pbo_cso_contact', models.CharField(blank=True, max_length=100)),
                ('pbo_cso_email', models.EmailField(blank=True, max_length=100, null=True)),
                ('pbo_cso_url', models.URLField(blank=True, null=True)),
                ('pbo_cso_link', models.CharField(blank=True, max_length=200, null=True)),
                ('pbo_cso_logo', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('pbo_cso_status', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='profile_attachments',
            fields=[
                ('cso_attachment_id', models.AutoField(primary_key=True, serialize=False)),
                ('cso_attachment_name', models.CharField(blank=True, max_length=255, null=True)),
                ('cso_attachment_description', models.CharField(blank=True, max_length=200, null=True)),
                ('cso_type', models.CharField(blank=True, max_length=255, null=True)),
                ('public_display', models.CharField(blank=True, max_length=200, null=True)),
                ('process', models.CharField(blank=True, max_length=200, null=True)),
                ('status', models.CharField(blank=True, default='Active', max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SignInDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(blank=True, max_length=220, null=True)),
                ('password', models.CharField(blank=True, max_length=220, null=True)),
                ('sign_in_date', models.DateTimeField(auto_now_add=True)),
                ('sign_out_date', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='system_process',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('process', models.CharField(blank=True, max_length=100, null=True)),
                ('description', models.CharField(blank=True, max_length=100, null=True)),
                ('duration', models.IntegerField(blank=True, null=True)),
                ('date_created', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='thematic_area',
            fields=[
                ('cso_id', models.AutoField(primary_key=True, serialize=False)),
                ('cso_name', models.CharField(blank=True, max_length=255, null=True)),
                ('cso_status', models.CharField(default='Active', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='user_roles',
            fields=[
                ('user_role_id', models.AutoField(primary_key=True, serialize=False)),
                ('user_role', models.CharField(blank=True, max_length=220, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='users',
            fields=[
                ('user_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('full_name', models.CharField(blank=True, max_length=220, null=True)),
                ('username', models.CharField(blank=True, max_length=220, null=True)),
                ('password', models.CharField(blank=True, max_length=220, null=True)),
                ('role', models.CharField(blank=True, max_length=100, null=True)),
                ('organization', models.CharField(blank=True, max_length=100, null=True)),
                ('email', models.EmailField(max_length=220)),
                ('CID', models.CharField(blank=True, max_length=11, null=True)),
                ('mobile_no', models.IntegerField(blank=True, null=True)),
                ('dob', models.DateTimeField(blank=True, null=True)),
                ('position_title', models.CharField(blank=True, max_length=100, null=True)),
                ('profile_pic', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]