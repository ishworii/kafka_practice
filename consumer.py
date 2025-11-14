from kafka import KafkaConsumer


consumer = KafkaConsumer(
    "events",
    bootstrap_servers="localhost:9092",
    auto_offset_reset="earliest",
    group_id="event-watchers",
)
print("Starting consumer ...Waiting for messages..")
print("-" * 20)
try:
    for message in consumer:
        print(f"Received: {message.value.decode('utf-8')}")
except KeyboardInterrupt:
    print("\nConsumer stopped..")
finally:
    consumer.close()
    print("Consumer closed..")