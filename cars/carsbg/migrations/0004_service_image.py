# Generated by Django 2.0.7 on 2018-07-07 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carsbg', '0003_auto_20180706_1740'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='image',
            field=models.ImageField(blank=True, upload_to='media/'),
        ),
    ]
