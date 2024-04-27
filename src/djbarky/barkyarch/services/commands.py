from abc import ABC, abstractmethod
from datetime import datetime
import sys
from database import DatabaseManager

# Assuming you have a similar DatabaseManager for your PMS
db = DatabaseManager("pms.db")

class Command(ABC):
    @abstractmethod
    def execute(self, data):
        pass

class CreatePatientsTableCommand(Command):
    def execute(self, data=None):
        db.create_table("patients", {
            "id": "integer primary key autoincrement",
            "name": "text not null",
            "date_of_birth": "text not null",
            "medical_history": "text",
        })

class AddPatientCommand(Command):
    def execute(self, data):
        db.add("patients", data)
        return "Patient added!"

class ListPatientsCommand(Command):
    def __init__(self, order_by="date_of_birth"):
        self.order_by = order_by

    def execute(self, data=None):
        return db.select("patients", order_by=self.order_by).fetchall()

class DeletePatientCommand(Command):
    def execute(self, data):
        db.delete("patients", {"id": data})
        return "Patient deleted!"

class EditPatientCommand(Command):
    def execute(self, data):
        db.update("patients", {"id": data["id"]}, data["update"])
        return "Patient updated!"

# You can include additional commands for HealthMetrics and TreatmentPlans, etc.

class QuitCommand(Command):
    def execute(self, data=None):
        sys.exit()
