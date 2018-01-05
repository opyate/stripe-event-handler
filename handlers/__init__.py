from models import db, Event
import importlib

def handle(event_json):

    event_type = event_json['type']
    print('Handling event type={}'.format(event_type), flush=True)
    print(event_json, flush=True)

    event = Event(event_json)
    db.session.add(event)
    db.session.commit()

    handler_module = 'handlers.' + event_type
    try:
        event_specific_handler = importlib.import_module(handler_module)
        event_specific_handler.handle(event_json)
    except ModuleNotFoundError:
        print('No handler for event_type={}'.format(event_type), flush=True)
