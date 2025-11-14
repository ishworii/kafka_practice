from kafka import KafkaConsumer
import json

def json_deserializer(data):
    return json.loads(data.decode("utf-8"))

def key_deserializer(data):
    return data.decode("utf-8")

# state
state_store = {}
print("Starting stateful processor..")



consumer = KafkaConsumer(
    "events",
    bootstrap_servers="localhost:9092",
    auto_offset_reset="earliest",
    group_id="stateful-processors",
    value_deserializer=json_deserializer,
    key_deserializer = key_deserializer,
)
print("-" * 20)
try:
    for message in consumer:
        user_id  = message.key
        action = message.value.get("action","unknown_action")
        state_store.setdefault(user_id,{})
        state_store[user_id].setdefault(action,0)
        state_store[user_id][action] += 1
        print(f"RECV (P{message.partition}): User {user_id}")
        print(f"-> Current State: {state_store[user_id]}")
except KeyboardInterrupt:
    print("\nConsumer stopped..")
    print("\nFINAL STATE")
    print(json.dumps(state_store,indent=2))
finally:
    consumer.close()
    print("Consumer closed..")