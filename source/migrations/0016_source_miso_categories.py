# Generated by Django 4.2.4 on 2024-12-10 05:12

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("source", "0015_remove_source_loc_location_source_loc_latitude_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="source",
            name="miso_categories",
            field=models.JSONField(blank=True, default=dict),
        ),
    ]
