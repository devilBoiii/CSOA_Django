# Generated by Django 5.0.6 on 2024-08-13 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cso_app', '0072_alter_cso_attachment_and_fees_overall_fines'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cso_attachment_and_fees',
            name='overall_fines',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]