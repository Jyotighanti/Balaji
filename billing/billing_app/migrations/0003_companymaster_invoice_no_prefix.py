# Generated by Django 5.1.3 on 2024-12-19 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('billing_app', '0002_rename_round_off_sale_round_off_amount'),
    ]

    operations = [
        migrations.AddField(
            model_name='companymaster',
            name='invoice_no_prefix',
            field=models.CharField(max_length=250, null=True),
        ),
    ]
