# Generated by Django 4.1.6 on 2023-02-26 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('card', '0009_card_hebrew_nikkud'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='hebrew_nikkud',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]