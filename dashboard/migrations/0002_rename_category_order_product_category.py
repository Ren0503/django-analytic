# Generated by Django 4.0 on 2021-12-23 01:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='category',
            new_name='product_category',
        ),
    ]
