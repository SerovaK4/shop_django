# Generated by Django 4.2.2 on 2023-07-18 22:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='email_verify',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='country',
            field=models.CharField(max_length=100, verbose_name='страна'),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254, unique=True, verbose_name='почта'),
        ),
    ]
