# Generated by Django 5.0.6 on 2024-08-13 05:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cso_app', '0066_remove_cso_fees_payment_amendment_fees_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='cso_fees_payment',
            name='amendment_fees',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='cso_fees_payment',
            name='amendment_type',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='cso_fees_payment',
            name='annual_general_report',
            field=models.FileField(blank=True, default='annual_general_report/index.html', null=True, upload_to='annual_general_report/'),
        ),
        migrations.AddField(
            model_name='cso_fees_payment',
            name='annual_report',
            field=models.FileField(blank=True, null=True, upload_to='annual_report/'),
        ),
        migrations.AddField(
            model_name='cso_fees_payment',
            name='audit_report',
            field=models.FileField(blank=True, null=True, upload_to='audit_report/'),
        ),
        migrations.AddField(
            model_name='cso_fees_payment',
            name='late_renewal_fees',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='cso_fees_payment',
            name='otp',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='cso_fees_payment',
            name='reject_reasons',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='cso_fees_payment',
            name='two_yrs_report',
            field=models.FileField(blank=True, null=True, upload_to='two_yrs_report/'),
        ),
        migrations.AlterField(
            model_name='cso_fees_payment',
            name='cso_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cso_app.cso_lists'),
        ),
        migrations.DeleteModel(
            name='cso_files_attachment',
        ),
    ]