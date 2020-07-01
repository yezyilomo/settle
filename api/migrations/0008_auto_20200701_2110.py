# Generated by Django 3.0.7 on 2020-07-01 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_auto_20200630_2128'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='apartment',
            name='payment_terms',
        ),
        migrations.RemoveField(
            model_name='apartment',
            name='payment_terms_unit',
        ),
        migrations.RemoveField(
            model_name='frame',
            name='payment_terms',
        ),
        migrations.RemoveField(
            model_name='frame',
            name='payment_terms_unit',
        ),
        migrations.RemoveField(
            model_name='hostel',
            name='payment_terms',
        ),
        migrations.RemoveField(
            model_name='hostel',
            name='payment_terms_unit',
        ),
        migrations.RemoveField(
            model_name='house',
            name='payment_terms',
        ),
        migrations.RemoveField(
            model_name='house',
            name='payment_terms_unit',
        ),
        migrations.RemoveField(
            model_name='office',
            name='payment_terms',
        ),
        migrations.RemoveField(
            model_name='office',
            name='payment_terms_unit',
        ),
        migrations.RemoveField(
            model_name='room',
            name='payment_terms',
        ),
        migrations.RemoveField(
            model_name='room',
            name='payment_terms_unit',
        ),
        migrations.AddField(
            model_name='property',
            name='payment_terms',
            field=models.TextField(blank=True, null=True),
        ),
    ]
