from django.test import RequestFactory, TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import Patient
from .views import PatientViewSet

class PatientTests(APITestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.patient = Patient.objects.create(
            id=1,
            name="John Doe",
            date_of_birth="1990-01-01",
            medical_history="No known allergies."
        )
        self.list_url = reverse("pms_app:patient-list")
        self.detail_url = reverse("pms_app:patient-detail", kwargs={"pk": self.patient.id})

    # 1. Create a patient
    def test_create_patient(self):
        data = {
            "name": "Jane Doe",
            "date_of_birth": "1992-02-02",
            "medical_history": "Asthmatic."
        }
        response = self.client.post(self.list_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Patient.objects.count(), 2)
        self.assertEqual(Patient.objects.get(id=2).name, "Jane Doe")

    # 2. List patients
    def test_list_patients(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)  # Assuming default pagination is off
        self.assertEqual(response.data[0]['name'], self.patient.name)

    # 3. Retrieve a patient
    def test_retrieve_patient(self):
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], self.patient.name)

    # 4. Delete a patient
    def test_delete_patient(self):
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Patient.objects.count(), 0)

    # 5. Update a patient
    def test_update_patient(self):
        data = {
            "name": "John Doe Updated",
            "date_of_birth": "1990-01-01",
            "medical_history": "No known allergies."
        }
        response = self.client.put(self.detail_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], "John Doe Updated")
