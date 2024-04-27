from django.db import transaction
from django.test import TestCase
from django.urls import reverse
from django.utils.timezone import localtime

from barkyarch.domain.model import Patient
from barkyarch.domain.model import Patient as DomainPatient
from barkyarch.services.commands import (
    AddPatientCommand,
    ListPatientsCommand,
    DeletePatientCommand,
    EditPatientCommand,
)


class TestPatientCommands(TestCase):
    def setUp(self):
        self.patient_1 = DomainPatient(
            id=1,
            name="John Doe",
            date_of_birth="1990-01-01",
            medical_history="No known allergies."
        )

        self.patient_2 = DomainPatient(
            id=2,
            name="Jane Smith",
            date_of_birth="1992-02-02",
            medical_history="Asthmatic."
        )

    def test_command_add_patient(self):
        add_command = AddPatientCommand()
        add_command.execute(self.patient_1)

        # Run checks
        # Check if one object is inserted
        self.assertEqual(Patient.objects.count(), 1)

        # Check if that object is the same as the one we inserted
        self.assertEqual(Patient.objects.get(id=1).name, self.patient_1.name)

    def test_command_list_patients(self):
        # Assuming ListPatientsCommand lists all patients and returns a list
        list_command = ListPatientsCommand()
        patient_list = list_command.execute()
        self.assertIn(self.patient_1, patient_list)
        self.assertIn(self.patient_2, patient_list)

    def test_command_delete_patient(self):
        delete_command = DeletePatientCommand()
        delete_command.execute(self.patient_1.id)
        self.assertEqual(Patient.objects.count(), 0)

    def test_command_edit_patient(self):
        edit_command = EditPatientCommand()
        updates = {"medical_history": "Updated history"}
        edit_command.execute(self.patient_1.id, updates)
        self.assertEqual(Patient.objects.get(id=1).medical_history, "Updated history")
