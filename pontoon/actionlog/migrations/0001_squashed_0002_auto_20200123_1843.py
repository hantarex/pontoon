# Generated by Django 1.11.28 on 2020-03-08 19:27
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("base", "0002_auto_20200322_1821"),
    ]

    operations = [
        migrations.CreateModel(
            name="ActionLog",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "action_type",
                    models.CharField(
                        choices=[
                            ("translation:created", "Translation created"),
                            ("translation:deleted", "Translation deleted"),
                            ("translation:approved", "Translation approved"),
                            ("translation:unapproved", "Translation unapproved"),
                            ("translation:rejected", "Translation rejected"),
                            ("translation:unrejected", "Translation unrejected"),
                            ("comment:added", "Comment added"),
                        ],
                        max_length=50,
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "entity",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="base.Entity",
                    ),
                ),
                (
                    "locale",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="base.Locale",
                    ),
                ),
                (
                    "performed_by",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="actions",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "translation",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="base.Translation",
                    ),
                ),
            ],
        ),
    ]
