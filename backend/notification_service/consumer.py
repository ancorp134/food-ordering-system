import json
from kafka import KafkaConsumer

def safe_deserialize(v):
    if v is None:
        return None
    try:
        return json.loads(v.decode("utf-8"))
    except json.JSONDecodeError:
        print(f"⚠️ Skipping invalid JSON: {v}")
        return None

consumer = KafkaConsumer(
    "order-events",
    bootstrap_servers=["localhost:9092"],
    group_id="notification-group",
    auto_offset_reset="earliest",
    enable_auto_commit=True,
    value_deserializer=safe_deserialize, # Use the safe function here
    key_deserializer=lambda k: k.decode("utf-8") if k else None,
)

print("📢 Notification Service started. Waiting for events...")

for message in consumer:
    event = message.value

    if event is None:
        continue

    

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
