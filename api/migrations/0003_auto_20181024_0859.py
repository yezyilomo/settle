# Generated by Django 2.0.4 on 2018-10-24 08:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20181024_0854'),
    ]

    operations = [
        migrations.RenameField(
            model_name='property',
            old_name='price_negotiationn',
            new_name='price_negotiation',
        ),
    ]