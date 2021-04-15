# Generated by Django 3.2 on 2021-04-15 13:29

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20210415_1130'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscriber',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='subscriber',
            name='updated',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
