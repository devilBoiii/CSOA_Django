# Generated by Django 5.0.6 on 2024-08-13 04:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cso_app', '0065_remove_cso_fees_payment_annual_general_report_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cso_fees_payment',
            name='amendment_fees',
        ),
        migrations.RemoveField(
            model_name='cso_fees_payment',
            name='amendment_type',
        ),
        migrations.RemoveField(
            model_name='cso_fees_payment',
            name='late_renewal_fees',
        ),
        migrations.RemoveField(
            model_name='cso_fees_payment',
            name='otp',
        ),
        migrations.AlterField(
            model_name='cso_fees_payment',
            name='cso_id',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
