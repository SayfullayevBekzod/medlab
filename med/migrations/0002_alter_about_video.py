# Generated by Django 5.0.3 on 2024-04-02 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("med", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="about",
            name="video",
            field=models.CharField(max_length=256),
        ),
    ]
