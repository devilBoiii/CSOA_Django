# Generated by Django 5.0.6 on 2024-08-26 05:17

import django_ckeditor_5.fields
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cso_app', '0087_alter_notifications_notifications_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='post_publish',
            name='post_description',
            field=django_ckeditor_5.fields.CKEditor5Field(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='notifications',
            name='notifications_id',
            field=models.UUIDField(default=uuid.UUID('8d0f06f7-82fe-4324-a414-29fa18574860'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='post_publish',
            name='post_id',
            field=models.UUIDField(default=uuid.UUID('42c1b1ff-8af6-40be-98e3-675d168adacb'), editable=False, unique=True),
        ),
    ]