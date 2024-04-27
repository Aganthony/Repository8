# pms_app/uow.py
from __future__ import annotations
import abc
from django.db import transaction
from adapters.repository import PatientRepository, HealthMetricRepository 
from barkyapi.models import Patient, HealthMetric  

class AbstractUnitOfWork(abc.ABC):
    patients: PatientRepository
    health_metrics: HealthMetricRepository  

    def __enter__(self) -> AbstractUnitOfWork:
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.rollback()

    @abc.abstractmethod
    def commit(self):
        raise NotImplementedError

    @abc.abstractmethod
    def rollback(self):
        raise NotImplementedError


class DjangoUnitOfWork(AbstractUnitOfWork):
    def __init__(self):
        self.patients = PatientRepository(Patient)
        self.health_metrics = HealthMetricRepository(HealthMetric) 

    def __enter__(self):
        transaction.set_autocommit(False)
        return super().__enter__()

    def __exit__(self, exc_type, exc_val, exc_tb):
        super().__exit__(exc_type, exc_val, exc_tb)
        transaction.set_autocommit(True)

    def commit(self):
        transaction.commit()

    def rollback(self):
        transaction.rollback()
