# Generated by Django 5.0.6 on 2024-07-31 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cso_app', '0053_rename_pubic_email_cso_lists_public_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trustee',
            name='appointed_date',
            field=models.DateField(null=True),
        ),
    ]