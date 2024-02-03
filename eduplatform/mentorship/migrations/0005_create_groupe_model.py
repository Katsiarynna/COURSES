# Generated by Django 5.0.1 on 2024-01-31 01:58

import django.db.models.deletion
import mentorship.mixins
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mentorship", "0004_create_email_model"),
        ("testing_system", "0007_create_attempt_model"),
    ]

    operations = [
        migrations.CreateModel(
            name="Group",
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
                ("group_name", models.CharField(max_length=50)),
                (
                    "course",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="testing_system.course",
                    ),
                ),
                (
                    "student",
                    models.ManyToManyField(
                        blank=True, default=None, to="mentorship.student"
                    ),
                ),
                (
                    "teacher",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="mentorship.teacher",
                    ),
                ),
            ],
            options={
                "verbose_name": "group",
                "verbose_name_plural": "groups",
            },
            bases=(models.Model, mentorship.mixins.DateTimeMixin),
        ),
    ]