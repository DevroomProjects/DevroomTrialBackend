# Generated by Django 3.2.10 on 2022-05-06 07:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0006_transaction_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='from_card',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='from_card', to='cards.card'),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='to_card',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='to_card', to='cards.card'),
        ),
    ]
