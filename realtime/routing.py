# routing.py
from channels.routing import route
from .consumers import websocket_receive, ws_connect, ws_disconnect

channel_routing = [
    route('websocket.connect', ws_connect),
    route('websocket.receive', websocket_receive),
    route("websocket.disconnect", ws_disconnect),
]
