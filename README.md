# Kafka Practice Project

This project is a simple Kafka setup with producers and consumers.

### Features

*   **Producer and Consumer:** A single producer and consumer setup.
*   **Multiple Consumers:** Support for multiple consumers.
*   **JSON Support:** Producers and consumers can handle JSON messages.
*   **Keyed Messages:** The producer can send messages with keys.

### Project Details

#### Docker Compose Setup

The `docker-compose.yml` file sets up a single Kafka broker using KRaft mode. It exposes the broker on port 9092.

#### `num_partitions`

The `KAFKA_NUM_PARTITIONS` is set to 3 in `docker-compose.yml`. This is the default number of partitions for any auto-created topics. When the producer sends a message to a topic for the first time, Kafka creates the topic with 3 partitions.

#### Producer

The `producer.py` script sends JSON messages to the `events` topic. Each message contains an `event_id`, `user_id`, `action`, and `timestamp`.

##### `user_id` as a Key

The `user_id` is a randomly chosen long string from a predefined list to simulate unique users. This `user_id` is used as the key for the Kafka message.

Using the `user_id` as a key is important because it ensures that all events for a specific user are sent to the same partition. Kafka's default partitioner uses a hash of the key to determine the partition, so the same key will always map to the same partition. This guarantees the order of processing for a specific user's events.

#### Consumer

The `consumer.py` script consumes messages from the `events` topic. It uses a `group_id` of "event-watchers", which allows multiple instances of the consumer to work together as a consumer group to process messages in parallel.


#### Event Processing
The `processor.py` scripts consumes and processed the events and shows the count of action for each user like following:

```json
{
  "sdsdsfsfsfasfasfasfasfa": {
    "purchase": 3,
    "view": 3,
    "click": 5
  },
  "sdfsdfsdf452535": {
    "add_to_cart": 5,
    "purchase": 3,
    "click": 4,
    "view": 2
  },
  "23124234234": {
    "add_to_cart": 2,
    "view": 3,
    "purchase": 2,
    "click": 2
  }
}
```