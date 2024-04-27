# bootstrap.py

from dependency_injector import containers, providers
from djbarky.barkyarch.services.message_bus import MessageBus
from  djbarky.barkyarch.services.events_handlers import PatientCreatedEventHandler, PatientUpdatedEventHandler
from  djbarky.barkyarch.services.commands import CreatePatientCommandHandler, UpdatePatientCommandHandler

# Define a container for your application services
class Container(containers.DeclarativeContainer):
    config = providers.Configuration()
    
    # Event handlers
    patient_created_event_handler = providers.Factory(PatientCreatedEventHandler)
    patient_updated_event_handler = providers.Factory(PatientUpdatedEventHandler)
    
    # Command handlers
    create_patient_command_handler = providers.Factory(CreatePatientCommandHandler)
    update_patient_command_handler = providers.Factory(UpdatePatientCommandHandler)


# Initialize the container
container = Container()
container.config.from_yaml('config.yml')

# Usage example:
def bootstrap():
    # You could set up your message bus and pass the handlers to it
    # For example:
    message_bus = MessageBus(
        patient_created_event_handler=container.patient_created_event_handler(),
        patient_updated_event_handler=container.patient_updated_event_handler(),
        create_patient_command_handler=container.create_patient_command_handler(),
        update_patient_command_handler=container.update_patient_command_handler(),
    )
    
    # Start listening to the message bus
    message_bus.start()

if __name__ == "__main__":
    bootstrap()
