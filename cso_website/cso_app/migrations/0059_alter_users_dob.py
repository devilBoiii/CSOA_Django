# Generated by Django 5.0.6 on 2024-08-02 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cso_app', '0058_alter_users_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='dob',
            field=models.DateField(blank=True, null=True),
        ),
    ]