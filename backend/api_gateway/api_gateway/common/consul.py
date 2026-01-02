import requests

CONSUL_URL = "http://localhost:8500"


def get_service(service_name):

    response = requests.get(
        f"{CONSUL_URL}/v1/health/service/{service_name}?passing=true",
        timeout=5
    )

    services = response.json()

    if not services:
        raise Exception(f"No healthy instance for {service_name}")

    service = services[0]["Service"]
    return service["Address"], service["Port"]