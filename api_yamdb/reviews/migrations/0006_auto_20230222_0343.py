# Generated by Django 3.2 on 2023-02-22 00:43

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("reviews", "0005_auto_20230222_0325"),
    ]

    operations = [
        migrations.RenameField(
            model_name="genretitle",
            old_name="genre_id",
            new_name="genre",
        ),
        migrations.RenameField(
            model_name="genretitle",
            old_name="title_id",
            new_name="title",
        ),
    ]
