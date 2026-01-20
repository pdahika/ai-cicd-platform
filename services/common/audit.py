import json, datetime

def audit(event, payload):
    record = {
        "event": event,
        "payload": payload,
        "timestamp": str(datetime.datetime.utcnow())
    }
    with open("audit.log", "a") as f:
        f.write(json.dumps(record) + "\n")
