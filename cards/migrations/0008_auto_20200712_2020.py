# Generated by Django 3.0.8 on 2020-07-12 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0007_auto_20200712_2015'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='status',
            field=models.CharField(choices=[('Неактивована', 'Неактивована'), ('Неактивована', 'Активована'), ('Неактивована', 'Прострочена')], max_length=20),
        ),
    ]