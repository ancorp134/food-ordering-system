from kafka import KafkaProducer
import json


producer = KafkaProducer(
    bootstrap_servers=["localhost:9092"],
    value_serializer=lambda v: json.dumps(v).encode("utf-8"),
    key_serializer=lambda k: str(k).encode("utf-8"),
    
    api_version=(3, 6, 0) 
)


def publish_event(event_type,key,payload):
    event = {
        "event_type" : event_type,
        "data" : payload
    }

    def on_send_success(record_metadata):
        print(f"✅ Successfully published to topic: {record_metadata.topic}")
        print(f"📍 Partition: {record_metadata.partition}")
        print(f"🔢 Offset: {record_metadata.offset}")

    def on_send_error(excp):
        print(f"❌ Failed to publish: {excp}")

    producer.send(  
        topic="order-events",
        key=key,
        value=event
    ).add_callback(on_send_success).add_errback(on_send_error)

    producer.flush()
