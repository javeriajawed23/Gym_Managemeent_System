from django.urls import path
from .consumers import NotificationConsumer
ws_pattern=[
	path('ws/notifications/',NotificationConsumer.as_asgi()),
]