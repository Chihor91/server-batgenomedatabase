# Generated by Django 4.2.4 on 2024-05-08 07:40

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("source", "0010_source_collection_name_source_institution_name_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="source",
            name="collection_name",
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name="source",
            name="institution_name",
            field=models.CharField(max_length=150),
        ),
    ]
