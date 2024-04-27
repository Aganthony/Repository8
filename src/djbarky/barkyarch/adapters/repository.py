
from typing import Set
import abc

from pms.domain import model as domain_model 
from pms_app import models as django_models 

class AbstractRepository(abc.ABC):
    """
    An abstract base class for the repository, can be used with any data storage strategy.
    """

    @abc.abstractmethod
    def add(self, entity):
        raise NotImplementedError

    @abc.abstractmethod
    def get(self, reference):
        raise NotImplementedError

    @abc.abstractmethod
    def list(self):
        raise NotImplementedError


class DjangoRepository(AbstractRepository):
    """
    A repository using the Django ORM as the data storage strategy.
    """

    def add(self, patient: domain_model.Patient):
        # Transforms the domain model to Django model and saves it to the database.
        django_model = django_models.Patient.from_domain(patient)
        django_model.save()

    def get(self, patient_id) -> domain_model.Patient:
        django_patient = django_models.Patient.objects.filter(id=patient_id).first()
        if django_patient:
            return django_patient.to_domain()

    def list(self):
        return [
            patient.to_domain() for patient in django_models.Patient.objects.all()
        ]

    def update(self, patient: domain_model.Patient):
        # Update the Django model corresponding to the domain model.
        django_patient = django_models.Patient.objects.filter(id=patient.id).first()
        if django_patient:
            # If you have fields to update, they would be set here
            # django_patient.name = patient.name, etc.
            django_patient.save()

