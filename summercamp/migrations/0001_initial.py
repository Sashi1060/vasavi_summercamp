from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Enquiry",
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
                ("name", models.CharField(max_length=100)),
                ("phone", models.CharField(max_length=15)),
                ("child_age", models.PositiveIntegerField()),
                (
                    "batch",
                    models.CharField(
                        choices=[
                            ("morning", "Morning (8-12 yrs, 10am-12pm)"),
                            ("afternoon", "Afternoon (12+ yrs, 3pm-5pm)"),
                        ],
                        max_length=20,
                    ),
                ),
                ("message", models.TextField(blank=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
