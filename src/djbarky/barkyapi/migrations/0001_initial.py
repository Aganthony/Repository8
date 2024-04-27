

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models

class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Patient",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=255)),
                ("date_of_birth", models.DateField()),
                ("medical_history", models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name="HealthMetric",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("type", models.CharField(max_length=100)),
                ("value", models.FloatField()),
                ("recorded_at", models.DateTimeField(auto_now_add=True)),
                ("patient", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="health_metrics", to="app.Patient")),
            ],
        ),
        migrations.CreateModel(
            name="TreatmentPlan",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("description", models.TextField()),
                ("start_date", models.DateField()),
                ("end_date", models.DateField()),
                ("patient", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="treatment_plans", to="app.Patient")),
            ],
        ),
    ]
