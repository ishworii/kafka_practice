from kafka import KafkaConsumer
import json

def json_deserializer(data):
    return json.loads(data.decode("utf-8"))

def key_deserializer(data):
    return data.decode("utf-8")


consumer = KafkaConsumer(
    "events",
    bootstrap_servers="localhost:9092",
    auto_offset_reset="earliest",
    group_id="event-watchers",
    value_deserializer=json_deserializer,
    key_deserializer = key_deserializer,
)
print("Starting consumer ...Waiting for messages..")
print("-" * 20)
try:
    for message in consumer:
        event_data = message.value
        print(f"RECV(Partition {message.partition},Key {message.key}):{event_data}")
        # print(f"->User {event_data['user_id']} performed action:{event_data['action']}")
except KeyboardInterrupt:
    print("\nConsumer stopped..")
finally:
    consumer.close()
    print("Consumer closed..")