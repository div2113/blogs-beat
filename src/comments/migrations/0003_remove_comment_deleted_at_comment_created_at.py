# Generated by Django 5.1.5 on 2025-02-13 07:57

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("comments", "0002_remove_comment_updated_at"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="comment",
            name="deleted_at",
        ),
        migrations.AddField(
            model_name="comment",
            name="created_at",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
    ]
