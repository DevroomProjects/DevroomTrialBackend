# Generated by Django 3.2.10 on 2022-05-04 14:49

import cards.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=32)),
                ('csc', models.CharField(max_length=3)),
                ('number', models.IntegerField(max_length=16)),
                ('expire', models.DateTimeField(default=cards.models.set_expire)),
            ],
        ),
    ]
