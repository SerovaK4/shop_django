# Generated by Django 4.2.2 on 2023-07-20 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_product_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='version',
            name='is_current',
            field=models.BooleanField(blank=True, default=True, null=True),
        ),
    ]