from __future__ import unicode_literals, absolute_import
import sys, os

module_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.insert(0, module_path)

from SmartApi.smartConnect import SmartConnect

# from SmartApi.webSocket import WebSocket
from SmartApi.smartApiWebsocket import SmartWebSocket

__all__ = ["SmartConnect", "SmartWebSocket"]
