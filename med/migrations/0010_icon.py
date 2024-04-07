# Generated by Django 5.0.3 on 2024-04-04 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("med", "0009_doctor_foto"),
    ]

    operations = [
        migrations.CreateModel(
            name="Icon",
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
                ("name", models.CharField(max_length=128)),
                ("link", models.CharField(max_length=128)),
            ],
        ),
    ]
