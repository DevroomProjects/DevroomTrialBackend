# Generated by Django 3.2.10 on 2022-05-04 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0002_card_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='type',
            field=models.CharField(choices=[('MasterCard', 'MasterCard'), ('Visa', 'Visa')], max_length=32),
        ),
    ]
