# Generated by Django 5.1.3 on 2024-11-11 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("library_management", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Books",
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
                ("author", models.CharField(max_length=200)),
                ("quantity", models.IntegerField(default=1)),
            ],
        ),
        migrations.AddField(
            model_name="books_to_be_bought",
            name="author",
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
