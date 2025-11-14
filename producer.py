import time
from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers="localhost:9092")


print("Starting producer..")
event_id = 1

try:
    while True:
        # messages as bytes
        message= f"Event #{event_id}: Timestamp:{time.time()}"
        print(f"Sending message : {message}")
        # send to events topic
        producer.send("events",value=message.encode("utf-8"))
        event_id += 1
        time.sleep(1)
except KeyboardInterrupt:
    print("Producer stopped..")
finally:
    producer.flush()
    producer.close()
    print("Producer closed..")