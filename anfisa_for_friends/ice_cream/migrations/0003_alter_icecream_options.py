# Generated by Django 3.2.16 on 2024-01-27 14:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ice_cream', '0002_auto_20240127_1733'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='icecream',
            options={'ordering': ('output_order', 'title'), 'verbose_name': 'мороженое', 'verbose_name_plural': 'Мороженое'},
        ),
    ]
