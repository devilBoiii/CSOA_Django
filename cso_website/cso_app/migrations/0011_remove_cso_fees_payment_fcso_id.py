# Generated by Django 5.0.6 on 2024-07-04 05:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cso_app', '0010_fcso_lists_amendment_fee_due_date_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cso_fees_payment',
            name='fcso_id',
        ),
    ]