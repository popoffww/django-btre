# Generated by Django 3.1.2 on 2020-10-25 09:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0002_listing_photo_main'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='listing',
            options={'verbose_name': 'Недвижимость', 'verbose_name_plural': 'Листинг'},
        ),
    ]
