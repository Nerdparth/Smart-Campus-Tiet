# Generated by Django 5.1.3 on 2024-11-11 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="books_to_be_bought",
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
                ("book_name", models.CharField(max_length=200)),
                ("quantity", models.IntegerField(default=1)),
                ("price", models.IntegerField(default=0)),
                ("remarks", models.CharField(default="nothing", max_length=2000)),
            ],
        ),
        migrations.CreateModel(
            name="Inventory",
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
                ("Budget", models.IntegerField(default=50000)),
            ],
        ),
    ]
