import os
from django.apps import AppConfig


class OrdersConfig(AppConfig):
    name = "orders"

    def ready(self):
        if os.environ.get("RUN_MAIN") != "true":
            return

        from order_service.common.consul import register_service
        register_service("order-service", 8004)
