import time
from kafka import KafkaProducer
import json
import random

def json_serializer(data):
    return json.dumps(data).encode("utf-8")

def key_serializer(data):
    return str(data).encode("utf-8")

producer = KafkaProducer(bootstrap_servers="localhost:9092",value_serializer=json_serializer,key_serializer=key_serializer)


print("Starting producer..")
event_id = 1
# actions example
actions = ["click","view","add_to_cart","purchase"]
# user ids example
user_ids = ["sdsdsfsfsfasfasfasfasfa","23124234234","sdfsdfsdf452535"]
try:
    while True:
        # messages as bytes
        message={
            "event_id" : event_id,
            "user_id" : random.choice(user_ids),
            "action" : random.choice(actions),
            "timestamp" : time.time(),
        }
        print(f"Sending message : {message}")
        # send to events topic
        producer.send("events",value=message,key=message["user_id"])
        event_id += 1
        time.sleep(0.5)
except KeyboardInterrupt:
    print("Producer stopped..")
finally:
    producer.flush()
    producer.close()
    print("Producer closed..")