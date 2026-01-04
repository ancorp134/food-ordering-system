import json
from kafka import KafkaConsumer


consumer = KafkaConsumer(
    "order-events",
    bootstrap_servers=["localhost:9092"],
    group_id="notification-group",   
    auto_offset_reset="earliest", 
    enable_auto_commit=True,
    value_deserializer=lambda v: json.loads(v.decode("utf-8")),
    key_deserializer=lambda k: k.decode("utf-8") if k else None,
)

print("📢 Notification Service started. Waiting for events...")

for message in consumer:
    event = message.value
    event_type = event.get("event_type")
    data = event.get("data")

    print("\n📩 New Event Received")
    print("Event Type:", event_type)
    print("Order ID:", data.get("order_id"))
    print("Customer ID:", data.get("customer_id"))
    print("Total Amount:", data.get("total_amount"))

    # Later:
    # send_email()
    # send_sms()
