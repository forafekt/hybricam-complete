# Generated by Django 3.0.7 on 2020-07-11 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscribe', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscribe',
            name='email',
            field=models.EmailField(blank=True, max_length=255, null=True, unique=True, verbose_name='Email Subscribe'),
        ),
    ]
