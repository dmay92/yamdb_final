# Generated by Django 3.2 on 2023-02-22 00:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("reviews", "0003_remove_title_rating"),
    ]

    operations = [
        migrations.AlterField(
            model_name="title",
            name="category",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="category",
                to="reviews.category",
                verbose_name="Slug категории",
            ),
        ),
        migrations.AlterField(
            model_name="title",
            name="genre",
            field=models.ManyToManyField(
                related_name="genre",
                through="reviews.GenreTitle",
                to="reviews.Genre",
                verbose_name="Slug жанра",
            ),
        ),
    ]
