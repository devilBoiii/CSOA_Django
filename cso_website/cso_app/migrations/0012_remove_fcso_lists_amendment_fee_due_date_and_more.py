# Generated by Django 5.0.6 on 2024-07-04 05:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cso_app', '0011_remove_cso_fees_payment_fcso_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fcso_lists',
            name='amendment_fee_due_date',
        ),
        migrations.RemoveField(
            model_name='mbo_lists',
            name='amendment_fee_due_date',
        ),
        migrations.RemoveField(
            model_name='pbo_lists',
            name='amendment_fee_due_date',
        ),
    ]