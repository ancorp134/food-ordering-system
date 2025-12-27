import requests
from django.conf import settings

CART_SERVICE_URL = "http://localhost:8003"



def get_cart(token):
    url = f"{CART_SERVICE_URL}/cart/"
    response = requests.get(
        url = url,
        headers= {
            'Authorization' : token
        },
        timeout=5
    )

    if response.status_code != 200:
        return None
    
    return response.json()



def clear_cart(token):
    url = f"{CART_SERVICE_URL}/cart/"

    requests.delete(
        url=url,
        headers={
            'Authorization' : token
        },
        timeout=5
    )
    
