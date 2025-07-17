import asyncio
import websockets
import json
from config import WS_PORT

connected = set()

async def echo(websocket):
    connected.add(websocket)
    try:
        async for message in websocket:
            await websocket.send(f"Received: {message}")
    finally:
        connected.remove(websocket)

async def broadcast(message):
    if connected:
        await asyncio.wait([ws.send(json.dumps(message)) for ws in connected])

def start_websocket_server():
    print(f"WebSocket server listening on ws://localhost:{WS_PORT}")
    asyncio.get_event_loop().run_until_complete(
        websockets.serve(echo, "0.0.0.0", WS_PORT)
    )
    asyncio.get_event_loop().run_forever()

if __name__ == "__main__":
    start_websocket_server()
