# Generated by Django 5.0.7 on 2024-07-18 14:48

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_user_name_alter_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.UUIDField(default=uuid.UUID('a60970c8-7c26-4319-9222-b9a6c6a59ac8'), primary_key=True, serialize=False),
        ),
    ]
