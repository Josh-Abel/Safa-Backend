# Generated by Django 4.1.6 on 2023-02-23 21:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('card', '0005_alter_card_shoresh'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
