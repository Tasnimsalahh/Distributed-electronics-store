# Generated by Django 5.0.4 on 2024-05-03 18:23

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Electronics_App', '0010_alter_cart_cart_id_alter_update_remaining_quantity_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='Cart_id',
            field=models.UUIDField(default=uuid.UUID('efef0408-b9e9-4f1a-95a0-55276f12103d'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='update',
            name='remaining_quantity',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='update',
            name='sold_quantity',
            field=models.IntegerField(default=1),
        ),
    ]