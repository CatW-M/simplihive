# Generated by Django 4.1.3 on 2023-01-10 19:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_alter_item_status'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Status',
        ),
    ]
