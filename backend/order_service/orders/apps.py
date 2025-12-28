import os
from django.apps import AppConfig


class OrdersConfig(AppConfig):
    name = "orders"

    def ready(self):
        # Prevent duplicate registration due to Django auto-reload
        if os.environ.get("RUN_MAIN") != "true":
            return

        from order_service.common.consul import register_service
        register_service(8004,"order_service")
