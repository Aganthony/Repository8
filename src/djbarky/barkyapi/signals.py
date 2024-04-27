import csv
from pathlib import Path

from django.core.files import File
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Patient  
@receiver(post_save, sender=Patient)
def log_patient_to_csv(sender, instance, **kwargs):
    print("I am a signal! I was called because a Patient was saved!")

    file = Path(__file__).resolve().parent.parent / "logs" / "patient_log.csv"
    print(f"Writing to {file}")

    with open(file, "a+", newline="") as csvfile:
        logfile = File(csvfile)
        logwriter = csv.writer(logfile, delimiter=",")
        logwriter.writerow([
            instance.id,
            instance.name,
            instance.date_of_birth,
            instance.medical_history,
        ])

    print(f"Logged patient data to {file}")
