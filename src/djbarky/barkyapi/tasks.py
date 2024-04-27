from celery import shared_task # type: ignore
from django.utils import timezone
from .models import Patient, Appointment  

@shared_task
def send_appointment_reminders():
    today = timezone.now().date()
    upcoming_appointments = Appointment.objects.filter(date__gte=today)
    
    reminders_sent = 0
    for appointment in upcoming_appointments:
        if (appointment.date - today).days == 1:  
            appointment.send_reminder()
            reminders_sent += 1
    
    return f"Sent {reminders_sent} appointment reminders."

@shared_task
def analyze_patient_health_data(patient_id: int):
    try:
        patient = Patient.objects.get(id=patient_id)
        # Let's assume we analyze health metrics to predict health risks
        health_risks = patient.analyze_health_metrics()
        patient.update_health_risks(health_risks)
        return f"Updated health risks for {patient.name}"
    except Patient.DoesNotExist:
        return "Patient not found"

