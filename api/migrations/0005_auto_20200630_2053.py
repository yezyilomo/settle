# Generated by Django 3.0.7 on 2020-06-30 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_user_full_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='room',
            old_name='unit_of_payment_terms',
            new_name='payment_terms_unit',
        ),
        migrations.AddField(
            model_name='room',
            name='price_rate_unit',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
