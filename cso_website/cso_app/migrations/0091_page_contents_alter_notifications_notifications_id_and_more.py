# Generated by Django 5.0.6 on 2024-08-30 09:06

import django_ckeditor_5.fields
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cso_app', '0090_post_publish_post_img_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='page_contents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content_id', models.UUIDField(default=uuid.UUID('76756933-7085-4d50-99f7-b6e0000f5081'), editable=False, unique=True)),
                ('content_img', models.ImageField(blank=True, null=True, upload_to='images/page_content/')),
                ('content_header', models.CharField(blank=True, max_length=225, null=True)),
                ('content_display', models.CharField(blank=True, max_length=225, null=True)),
                ('content_created', models.DateField(auto_now_add=True, null=True)),
                ('contents', django_ckeditor_5.fields.CKEditor5Field(blank=True, null=True)),
                ('page', models.CharField(blank=True, max_length=225, null=True)),
                ('attachments', models.CharField(blank=True, default='No Attachment', max_length=225, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='notifications',
            name='notifications_id',
            field=models.UUIDField(default=uuid.UUID('0dd7f0c5-8936-4f7b-9bd5-192ab02cc7e3'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='post_publish',
            name='attachments',
            field=models.CharField(blank=True, default='No Attachment', max_length=225, null=True),
        ),
        migrations.AlterField(
            model_name='post_publish',
            name='post_id',
            field=models.UUIDField(default=uuid.UUID('4c9112cf-0ab9-4301-9249-30e40ffe985b'), editable=False, unique=True),
        ),
        migrations.AlterField(
            model_name='post_publish',
            name='post_img',
            field=models.ImageField(blank=True, null=True, upload_to='images/posts/'),
        ),
        migrations.AlterField(
            model_name='post_publish',
            name='published_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
