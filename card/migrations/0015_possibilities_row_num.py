# Generated by Django 4.1.6 on 2023-03-03 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('card', '0014_possibilities_english_dict_possibilities_hebrew_dict'),
    ]

    operations = [
        migrations.AddField(
            model_name='possibilities',
            name='row_num',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
