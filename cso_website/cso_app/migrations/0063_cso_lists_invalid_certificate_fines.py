# Generated by Django 5.0.6 on 2024-08-08 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cso_app', '0062_feedbackform_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='cso_lists',
            name='invalid_certificate_fines',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]