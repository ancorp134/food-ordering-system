import requests

CONSUL_URL = "http://localhost:8500"

def register_service(service_port,service_name):
    service_id = f"{service_name}-{service_port}"
    address = "127.0.0.1"


    payload = {
        "ID" : service_id,
        "Name" : service_name,
        "Address" : address,
        "Port" : service_port,
        "Check": {
            "HTTP": f"http://{address}:{service_port}/health/",
            "Interval": "10s"
        }
    }


    try:
        response = requests.put(
            f"{CONSUL_URL}/v1/agent/service/register",
            json=payload,
            timeout=5
        )

        if response.status_code == 200:
            print(f"✅ {service_name} registered with Consul")
        else:
            print(f"❌ Failed to register {service_name}: {response.text}")

    except Exception as e:
        print(f"❌ Consul registration error: {e}")