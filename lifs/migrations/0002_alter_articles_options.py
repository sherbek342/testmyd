# Generated by Django 4.2.3 on 2023-07-19 15:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lifs', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='articles',
            options={'verbose_name': 'Новость', 'verbose_name_plural': 'Новости'},
        ),
    ]
