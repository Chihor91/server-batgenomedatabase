# Generated by Django 4.2.4 on 2024-12-10 08:29

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("source", "0018_accessioncounter"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="isolate",
            name="raw_accession_no",
        ),
    ]
