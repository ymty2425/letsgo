from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from typing import List, Dict
from fastapi.staticfiles import StaticFiles
import asyncio

app = FastAPI()

app.mount("/static", StaticFiles(directory="webapp/static"), name="static")

class ConnectionManager:

    def __init__(self):
        self.active_connections: List[WebSocket] = []
        self.usernames: dict[WebSocket, str] = {}
        self.lock = asyncio.Lock()

    async def connect(self, websocket: WebSocket, username: str):
        """
        Accept a new WebSocket connection and add it to the active connections list.

        Args:
        websocket (WebSocket): The WebSocket connection to add.
        username (str): The username of the connecting client.
        """
        await websocket.accept()
        self.active_connections.append(websocket)
        self.usernames[websocket] = username

    def disconnect(self, websocket: WebSocket):
        """
        Remove a WebSocket connection from the active connections list.

        Args:
        websocket (WebSocket): The WebSocket connection to remove.
        """
        self.active_connections.remove(websocket)
        del self.usernames[websocket]

    async def broadcast(self, message: str):
        """
        Send a message to all active WebSocket connections.

        Args:
        message (str): The message to broadcast.
        """
        for connection in self.active_connections:
            await connection.send_text(message)

manager = ConnectionManager()

@app.get("/")
async def read_root():
    return {"message": "Welcome to the FastAPI chat application"}

@app.websocket("/ws/{username}")

async def websocket_endpoint(websocket: WebSocket, username: str):
    """
    Create a webSocket endpoint to handle client connections and messaging.

    Args:
    websocket (WebSocket): The WebSocket connection.
    username (str): The username of the connecting client.
    """
    await manager.connect(websocket, username)
    try:
        while True:
            data = await websocket.receive_text()
            message = f"{username}: {data}"
            await manager.broadcast(message)
    except WebSocketDisconnect:
        await manager.disconnect(websocket)
        message = f"{username} has left the chat"
        await manager.broadcast(message)