# Generated by Django 4.2.4 on 2023-09-06 11:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('taxonomy', '0004_taxonomy'),
    ]

    operations = [
        migrations.CreateModel(
            name='Host',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('common_name', models.CharField(max_length=100)),
                ('host_type', models.CharField(max_length=50)),
                ('host_taxonomy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hosts', to='taxonomy.taxonomy')),
            ],
            options={
                'verbose_name_plural': 'hosts',
            },
        ),
    ]