from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from chat.consumers import ChatConsumer
from joystick.consumers import JoyConsumers
from connect.consumers import ConnectConsumers
from django.urls import re_path

application = ProtocolTypeRouter({
    'websocket': AuthMiddlewareStack(
        URLRouter([
            re_path(r'ws/chat/(?P<room_name>\w+)/$', ChatConsumer),
            re_path(r'ws/joy/$', JoyConsumers),
            re_path(r'ws/$', ConnectConsumers),
        ])
    )
})