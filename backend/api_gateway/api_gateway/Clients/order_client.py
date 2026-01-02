import requests
from api_gateway.common.consul import get_service


class OrderServiceClient:

    def __init__(self,auth_header):
        self.auth_header = auth_header
        address,port = get_service("order-service")
        self.base_url = f"http://127.0.0.1:{port}"

    
    def _headers(self):
        
        return {
            "Content-Type": "application/json",
            "Authorization": self.auth_header
        }
    
    def checkout(self,data):
        return requests.post(
            f"{self.base_url}/order/checkout/",
            headers=self._headers(),
            json=data,
            timeout=5
        )
    

    def myorders(self):
        return requests.get(
            f"{self.base_url}/orders/me/",
            headers=self._headers(),
            timeout=5

        )