import asyncio
import websockets

async def echo(websocket):
    async for message in websocket:
        print(f"Server received: {message}")
        await websocket.send(f"Server says: {message}")

async def main():
    async with websockets.serve(echo, "localhost", 8765):
        print("WebSocket server started at ws://localhost:8765")
        await asyncio.Future()  # Keep the server running

if __name__ == "__main__":
    asyncio.run(main())
