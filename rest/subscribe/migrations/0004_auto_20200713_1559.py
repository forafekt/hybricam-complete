# Generated by Django 3.0.7 on 2020-07-13 13:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('subscribe', '0003_auto_20200711_1705'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='subscribe',
            options={'ordering': ('created_at',)},
        ),
    ]