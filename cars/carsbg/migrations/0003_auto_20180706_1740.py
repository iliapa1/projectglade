# Generated by Django 2.0.7 on 2018-07-06 14:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('carsbg', '0002_auto_20180706_1729'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='city',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='carsbg.City'),
        ),
    ]