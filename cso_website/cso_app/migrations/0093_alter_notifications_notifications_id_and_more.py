# Generated by Django 5.0.6 on 2024-09-17 08:55

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cso_app', '0092_rename_page_page_contents_website_page_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notifications',
            name='notifications_id',
            field=models.UUIDField(default=uuid.UUID('1164e05a-b7a3-4f6d-a4c5-666bb620861a'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='page_contents',
            name='content_id',
            field=models.UUIDField(default=uuid.UUID('4f394dcd-4d4a-467f-be2c-175aef4bd1bc'), editable=False, unique=True),
        ),
        migrations.AlterField(
            model_name='post_publish',
            name='post_id',
            field=models.UUIDField(default=uuid.UUID('59d4435d-4bed-4803-bddf-262a49bcdbda'), editable=False, unique=True),
        ),
    ]