# Generated by Django 3.0.8 on 2020-07-12 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0006_auto_20200712_1611'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='number',
            field=models.CharField(max_length=16),
        ),
    ]
