from djbarky.barkyarch.services.commands import AddPatientCommand, DeletePatientCommand
from djbarky.barkyarch.services.handlers import handle_add_patient, handle_delete_patient, handle_update_patient


class MessageBus:
    def __init__(self):
        self.command_handlers = {
            AddPatientCommand: handle_add_patient,
            
            DeletePatientCommand: handle_delete_patient
        }

    def handle(self, command):
        handler = self.command_handlers[type(command)]
        return handler(command)
