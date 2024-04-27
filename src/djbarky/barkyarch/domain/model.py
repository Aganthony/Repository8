from datetime import date

class Patient:
    """
    Patient domain model for the Patient Monitoring System.
    This model represents a patient with basic health record details.
    """

    def __init__(self, id, name, date_of_birth, medical_history):
        self.id = id
        self.name = name
        self.date_of_birth = date_of_birth
        self.medical_history = medical_history

    def __str__(self):
        return f"Patient: {self.name}, DOB: {self.date_of_birth}"

    def update_medical_history(self, new_history):
        """
        Updates the medical history of the patient.
        """
        self.medical_history = new_history
