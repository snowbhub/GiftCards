# Generated by Django 3.0.8 on 2020-07-12 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0008_auto_20200712_2020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='number',
            field=models.CharField(max_length=16, unique=True),
        ),
    ]
