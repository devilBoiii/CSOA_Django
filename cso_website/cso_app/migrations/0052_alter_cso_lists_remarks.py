# Generated by Django 5.0.6 on 2024-07-30 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cso_app', '0051_alter_cso_lists_fax'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cso_lists',
            name='remarks',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]