# Generated by Django 3.1.7 on 2021-03-22 11:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0006_auto_20210322_1345'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='owner_id',
            new_name='owner',
        ),
    ]
