import os
import sys
from pathlib import Path


loc = Path(__file__).resolve().parent.parent.parent / "pms_project"

print(f"loc: {loc}")

sys.path.append(str(loc))


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pms_project.settings")

import django
from django.apps import apps

# Initialize Django
django.setup()

settings_list = dir(django.conf.settings)
print(str(settings_list))

if apps.ready:
    print("Apps are ready")

    PatientModel = apps.get_model("health", "Patient")

    PatientModel.objects.create(
        id=1,
        name="John Doe",
        date_of_birth="1990-01-01",
        medical_history="Test history",
    )
    PatientModel.objects.create(
        id=2,
        name="Jane Smith",
        date_of_birth="1992-02-02",
        medical_history="Test history 2",
    )
    print("Patients: ", PatientModel.objects.all())

    # Clean up test data
    PatientModel.objects.all().delete()
