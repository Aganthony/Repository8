from datetime import date
from typing import Optional

class Patient:
    """
    Patient domain model for the Patient Monitoring System.
    """

    def __init__(self, id: int, name: str, date_of_birth: date, medical_history: Optional[str]):
        self.id = id
        self.name = name
        self.date_of_birth = date_of_birth
        self.medical_history = medical_history or ""

    def __str__(self):
        return f"Patient: {self.name} (DOB: {self.date_of_birth})"

class HealthMetric:
    """
    HealthMetric domain model to track a patient's health readings.
    """

    def __init__(self, id: int, patient_id: int, type: str, value: float, recorded_at: date):
        self.id = id
        self.patient_id = patient_id
        self.type = type
        self.value = value
        self.recorded_at = recorded_at

    def __str__(self):
        return f"{self.type}: {self.value} (Recorded at: {self.recorded_at})"


class TreatmentPlan:
    """
    TreatmentPlan domain model for managing a patient's treatment.
    """

    def __init__(self, id: int, patient_id: int, description: str, start_date: date, end_date: date):
        self.id = id
        self.patient_id = patient_id
        self.description = description
        self.start_date = start_date
        self.end_date = end_date

    def __str__(self):
        return f"Treatment Plan for Patient ID {self.patient_id} from {self.start_date} to {self.end_date}"
