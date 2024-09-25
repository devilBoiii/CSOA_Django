# Generated by Django 5.0.6 on 2024-07-17 05:27

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cso_app', '0033_delete_cso_fees_payment'),
    ]

    operations = [
        migrations.CreateModel(
            name='cso_fees_payment',
            fields=[
                ('payment_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('cso_name', models.CharField(blank=True, max_length=200, null=True)),
                ('bank_type', models.CharField(blank=True, max_length=100, null=True)),
                ('account_number', models.CharField(blank=True, max_length=100, null=True)),
                ('user_name', models.CharField(blank=True, max_length=100, null=True)),
                ('user_email', models.EmailField(blank=True, max_length=200, null=True)),
                ('otp', models.IntegerField(blank=True, null=True)),
                ('account_name', models.CharField(blank=True, max_length=200, null=True)),
                ('amendment_type', models.CharField(blank=True, max_length=200, null=True)),
                ('amendment_fees', models.IntegerField(blank=True, null=True)),
                ('user_cid', models.CharField(blank=True, max_length=200, null=True)),
                ('fees_payment_type', models.CharField(blank=True, max_length=100, null=True)),
                ('mobile_number', models.CharField(blank=True, max_length=100, null=True)),
                ('late_renewal_fees', models.CharField(blank=True, max_length=100, null=True)),
                ('amount_paid', models.CharField(blank=True, max_length=150, null=True)),
                ('payment_date', models.DateTimeField(auto_now_add=True)),
                ('overall_fines', models.DecimalField(decimal_places=2, max_digits=15)),
                ('status', models.CharField(blank=True, max_length=100, null=True)),
                ('reject_reasons', models.CharField(blank=True, max_length=500, null=True)),
                ('annual_report', models.FileField(blank=True, null=True, upload_to='annual_report/')),
                ('audit_report', models.FileField(blank=True, null=True, upload_to='audit_report/')),
                ('two_yrs_report', models.FileField(blank=True, null=True, upload_to='two_yrs_report/')),
                ('annual_general_report', models.FileField(blank=True, null=True, upload_to='annual_general_report/')),
                ('cso_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cso_app.cso_lists')),
            ],
        ),
    ]