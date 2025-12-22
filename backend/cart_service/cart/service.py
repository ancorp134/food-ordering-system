import json
from django.conf import settings
from django.core.cache import cache



def cart_key(customer_id):
    return f"cart:{customer_id}"


def get_cart(customer_id):
    data= cache.get(cart_key(customer_id))
    return json.loads(data) if data else None

def save_cart(customer_id,cart_data):
    cache.set(
        cart_key(customer_id),
        json.dumps(cart_data),
        timeout=settings.TTL
    )


def delete_cart(customer_id):
    cache.delete(get_cart(customer_id))