# Generated by Django 5.0.6 on 2024-08-14 04:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cso_app', '0075_cso_attachment_and_fees_cso_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='cso_attachment_and_fees',
            name='renewal_fees',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]