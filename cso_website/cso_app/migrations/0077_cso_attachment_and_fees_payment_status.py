# Generated by Django 5.0.6 on 2024-08-14 04:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cso_app', '0076_cso_attachment_and_fees_renewal_fees'),
    ]

    operations = [
        migrations.AddField(
            model_name='cso_attachment_and_fees',
            name='payment_status',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]