# Generated by Django 4.1.6 on 2023-02-23 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('card', '0004_alter_card_example_alter_card_form_alter_card_note'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='shoresh',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
