
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("med", "0024_department"),
    ]

    operations = [
        migrations.AlterField(
            model_name="department",
            name="tab",
            field=models.IntegerField(),
        ),
    ]
