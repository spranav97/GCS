from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
import chat.routing,joystick.routing

application = ProtocolTypeRouter({
    'websocket': AuthMiddlewareStack(
        URLRouter(
            #chat.routing.websocket_urlpatterns
            joystick.routing.websocket_urlpatterns
        )

    )
})