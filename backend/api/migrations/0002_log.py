# Generated by Django 5.0.3 on 2024-03-31 17:59

import api.adapters.outbound.database.models.utils
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Log",
            fields=[
                (
                    "id",
                    models.CharField(
                        default=api.adapters.outbound.database.models.utils.id_generator,
                        editable=False,
                        max_length=16,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("content", models.CharField(max_length=200)),
                (
                    "level",
                    models.CharField(
                        choices=[
                            ("INFO", "info"),
                            ("WARNING", "warning"),
                            ("ERROR", "error"),
                        ],
                        default="INFO",
                        max_length=12,
                    ),
                ),
                (
                    "executed_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="executed_at"),
                ),
                (
                    "run",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="api.run"
                    ),
                ),
            ],
        ),
    ]
