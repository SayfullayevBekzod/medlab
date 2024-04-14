# Generated by Django 5.0.3 on 2024-04-13 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("med", "0018_doctor_icon"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="doctor",
            name="icon",
        ),
        migrations.AddField(
            model_name="doctor",
            name="icon",
            field=models.ManyToManyField(
                null=True, related_name="doctor", to="med.icon"
            ),
        ),
    ]