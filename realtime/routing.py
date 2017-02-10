# routing.py
from channels.routing import route
from .consumers import websocket_receive

channel_routing = {
    'websocket.receive': websocket_receive,
}
