# Generated by Django 4.1.6 on 2023-02-23 23:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('card', '0007_card_timestamp'),
    ]

    operations = [
        migrations.RenameField(
            model_name='card',
            old_name='form',
            new_name='binyan',
        ),
        migrations.AddField(
            model_name='card',
            name='gender',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
