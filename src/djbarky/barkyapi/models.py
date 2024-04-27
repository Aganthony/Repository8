from django.db import models
from barkyarch.domain import model as domain_model  

# Create your models here.
class Patient(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    medical_history = models.TextField(blank=True)

    def __str__(self):
        return self.name
    
    @staticmethod
    def update_from_domain(domain_patient: domain_model.Patient):
        try:
            patient = Patient.objects.get(id=domain_patient.id)
        except Patient.DoesNotExist:
            patient = Patient(id=domain_patient.id)

        patient.name = domain_patient.name
        patient.date_of_birth = domain_patient.date_of_birth
        patient.medical_history = domain_patient.medical_history
        patient.save()

    def to_domain(self) -> domain_model.Patient:
        return domain_model.Patient(
            id=self.id,
            name=self.name,
            date_of_birth=self.date_of_birth,
            medical_history=self.medical_history,
        )

class HealthMetric(models.Model):
    patient = models.ForeignKey(Patient, related_name='health_metrics', on_delete=models.CASCADE)
    type = models.CharField(max_length=100)
    value = models.FloatField()
    recorded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.type} for {self.patient.name}: {self.value}"

class TreatmentPlan(models.Model):
    patient = models.ForeignKey(Patient, related_name='treatment_plans', on_delete=models.CASCADE)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f"Treatment Plan for {self.patient.name} starting on {self.start_date}"

    # Meta class to define ordering or any other model settings
    class Meta:
        ordering = ['start_date']
