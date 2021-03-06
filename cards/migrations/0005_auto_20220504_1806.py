# Generated by Django 3.2.10 on 2022-05-04 15:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0004_auto_20220504_1802'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='card',
            name='balance',
            field=models.FloatField(default=100),
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField()),
                ('from_card', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='from_card', to='cards.card')),
                ('to_card', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='to_card', to='cards.card')),
            ],
        ),
    ]
