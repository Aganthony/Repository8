

class Event:
    pass

class PatientCreatedEvent(Event):
    def __init__(self, patient_id, data):
        self.patient_id = patient_id
        self.data = data

class PatientUpdatedEvent(Event):
    def __init__(self, patient_id, data):
        self.patient_id = patient_id
        self.data = data

class EventHandler:
    def handle(self, event):
        raise NotImplementedError("Event handlers must implement the handle method")

class PatientCreatedEventHandler(EventHandler):
    def handle(self, event):
        if not isinstance(event, PatientCreatedEvent):
            return
        # Handle the PatientCreatedEvent
        # Implement the logic that should occur after a patient is created
        print(f"Handling patient created event for patient id: {event.patient_id}")

class PatientUpdatedEventHandler(EventHandler):
    def handle(self, event):
        if not isinstance(event, PatientUpdatedEvent):
            return
        # Handle the PatientUpdatedEvent
        # Implement the logic that should occur after a patient is updated
        print(f"Handling patient updated event for patient id: {event.patient_id}")

# This function might be called by your message bus to dispatch events to the appropriate handler
def dispatch(event):
    # In a real scenario, this could be replaced with more complex logic
    # to dynamically select the appropriate handler for the event.
    if isinstance(event, PatientCreatedEvent):
        handler = PatientCreatedEventHandler()
    elif isinstance(event, PatientUpdatedEvent):
        handler = PatientUpdatedEventHandler()
    else:
        raise ValueError("Unknown event type")
    
    handler.handle(event)
