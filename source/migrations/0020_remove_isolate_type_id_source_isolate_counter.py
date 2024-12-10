# Generated by Django 4.2.4 on 2024-12-10 08:39

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("source", "0019_remove_isolate_raw_accession_no"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="isolate",
            name="type_id",
        ),
        migrations.AddField(
            model_name="source",
            name="isolate_counter",
            field=models.IntegerField(default=0),
        ),
    ]