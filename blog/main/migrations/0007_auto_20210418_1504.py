# Generated by Django 3.2 on 2021-04-18 15:04

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20210415_1329'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(verbose_name='Комментарий')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'verbose_name': 'Комментарий',
                'verbose_name_plural': 'Комментарии',
            },
        ),
        migrations.AlterField(
            model_name='author',
            name='email',
            field=models.EmailField(max_length=50, null=True, verbose_name='Email автора'),
        ),
        migrations.AlterField(
            model_name='author',
            name='name',
            field=models.CharField(max_length=100, null=True, verbose_name='Имя автора'),
        ),
    ]
