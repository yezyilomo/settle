# Generated by Django 3.0.7 on 2020-07-01 22:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_auto_20200701_2110'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='land',
            name='length_unit',
        ),
        migrations.AlterField(
            model_name='land',
            name='area',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='land',
            name='length',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='land',
            name='width',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
