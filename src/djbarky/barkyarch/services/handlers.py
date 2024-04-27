from domain.model import Patient

def handle_add_patient(command):
    Patient.objects.create(
        name=command.name,
        date_of_birth=command.date_of_birth,
        medical_history=command.medical_history
    )

def handle_update_patient(command):
    patient = Patient.objects.get(id=command.patient_id)
    for attr, value in command.updates.items():
        setattr(patient, attr, value)
    patient.save()

def handle_delete_patient(command):
    patient = Patient.objects.get(id=command.patient_id)
    patient.delete()
