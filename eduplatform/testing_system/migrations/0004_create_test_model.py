# Generated by Django 5.0.1 on 2024-01-31 01:32

import django.db.models.deletion
import mentorship.mixins
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mentorship", "0004_create_email_model"),
        ("testing_system", "0003_create_article_model"),
    ]

    operations = [
        migrations.CreateModel(
            name="Test",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=100)),
                ("description", models.CharField(max_length=150)),
                ("is_open", models.BooleanField(default=False)),
                (
                    "teacher",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="mentorship.teacher",
                    ),
                ),
                (
                    "topic",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="testing_system.topic",
                    ),
                ),
            ],
            options={
                "verbose_name": "test",
                "verbose_name_plural": "tests",
            },
            bases=(models.Model, mentorship.mixins.DateTimeMixin),
        ),
    ]
