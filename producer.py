import time
from kafka import KafkaProducer
import json
import random

def json_serializer(data):
    return json.dumps(data).encode("utf-8")

producer = KafkaProducer(bootstrap_servers="localhost:9092",value_serializer=json_serializer)


print("Starting producer..")
event_id = 1
# actions example
actions = ["click","view","add_to_cart","purchase"]

try:
    while True:
        # messages as bytes
        message={
            "event_id" : event_id,
            "user_id" : random.randint(100,1000),
            "action" : random.choice(actions),
            "timestamp" : time.time(),
        }
        print(f"Sending message : {message}")
        # send to events topic
        producer.send("events",value=message)
        event_id += 1
        time.sleep(1)
except KeyboardInterrupt:
    print("Producer stopped..")
finally:
    producer.flush()
    producer.close()
    print("Producer closed..")