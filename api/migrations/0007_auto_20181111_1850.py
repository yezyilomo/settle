# Generated by Django 2.1.2 on 2018-11-11 18:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_auto_20181029_2101'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feature',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=256)),
                ('value', models.CharField(blank=True, max_length=256)),
            ],
        ),
        migrations.AlterField(
            model_name='phone',
            name='owner',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='phones', to='api.PropertyOwner'),
        ),
        migrations.AlterField(
            model_name='property',
            name='potentials',
            field=models.ManyToManyField(blank=True, related_name='potentials', to='api.Potential'),
        ),
        migrations.AlterField(
            model_name='property',
            name='services',
            field=models.ManyToManyField(blank=True, related_name='services', to='api.Service'),
        ),
        migrations.AddField(
            model_name='feature',
            name='property',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='other_features', to='api.Property'),
        ),
    ]