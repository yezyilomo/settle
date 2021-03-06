# Generated by Django 3.0.7 on 2020-08-26 05:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0016_auto_20200809_1410'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Room',
            new_name='SingleRoom',
        ),
        migrations.AlterField(
            model_name='property',
            name='contact',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.Contact'),
        ),
        migrations.AlterField(
            model_name='property',
            name='location',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.Location'),
        ),
    ]
