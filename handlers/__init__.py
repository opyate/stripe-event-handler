from models import db, Event


def handle(event_json):

    event_type = event_json['type']
    print('Handling event type={}'.format(event_type), flush=True)
    print(event_json, flush=True)

    event = Event(event_json)
    db.session.add(event)
    db.session.commit()
