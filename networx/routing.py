
from channels.routing import route
from .consumers import ws_message, ws_connect, ws_disconnect
from otree.channels.routing import channel_routing

channel_routing += [
    route("websocket.connect", ws_connect, path=r"^/qchannel"),
    route("websocket.receive", ws_message, path=r'^/qchannel'),
    route("websocket.disconnect", ws_disconnect, path=r"^/qchannel"),
]


print('CHANNEL ROUTING:', channel_routing)
