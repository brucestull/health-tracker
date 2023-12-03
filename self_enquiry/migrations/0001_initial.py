# Generated by Django 4.1.7 on 2023-12-03 23:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Journal",
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
                (
                    "created",
                    models.DateTimeField(
                        auto_now_add=True,
                        help_text="The date and time this object was created.",
                        verbose_name="Created",
                    ),
                ),
                (
                    "updated",
                    models.DateTimeField(
                        auto_now=True,
                        help_text="The date and time this object was last updated.",
                        verbose_name="Updated",
                    ),
                ),
                (
                    "title",
                    models.CharField(
                        blank=True,
                        help_text="Optional - 100 characters or fewer",
                        max_length=100,
                        null=True,
                        verbose_name="Journal Title",
                    ),
                ),
                (
                    "content",
                    models.TextField(
                        help_text="Required", verbose_name="Journal Content"
                    ),
                ),
                (
                    "author",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="journals",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="GrowthOpportunity",
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
                (
                    "created",
                    models.DateTimeField(
                        auto_now_add=True,
                        help_text="The date and time this object was created.",
                        verbose_name="Created",
                    ),
                ),
                (
                    "updated",
                    models.DateTimeField(
                        auto_now=True,
                        help_text="The date and time this object was last updated.",
                        verbose_name="Updated",
                    ),
                ),
                (
                    "question",
                    models.TextField(help_text="Required", verbose_name="Question"),
                ),
                (
                    "author",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="growth_opportunities",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "Growth Opportunity",
                "verbose_name_plural": "Growth Opportunities",
            },
        ),
    ]