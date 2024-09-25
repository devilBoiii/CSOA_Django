# Generated by Django 5.0.6 on 2024-07-29 04:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cso_app', '0043_rename_cso_name_cso_types_cso_type_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cso_lists',
            name='amendment_fee_due_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='cso_lists',
            name='application_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='cso_lists',
            name='late_renewal_fee_due_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='cso_lists',
            name='renewal_fee_due_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='cso_lists',
            name='reporting_time',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]