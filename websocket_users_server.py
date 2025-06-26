import asyncio
import websockets
from websockets import ServerConnection


async def echo(websocket: ServerConnection):
    # Получаем сообщения от клиента
    async for message in websocket:
        print(f"Получено сообщение от пользователя: {message}")
        # Отправляем пять пронумерованных ответов
        for i in range(1, 6):
            response = f"{i} Сообщение пользователя: {message}"
            await websocket.send(response)


async def main():
    # Запускаем сервер на localhost:8765
    server = await websockets.serve(echo, "localhost", 8765)
    print("WebSocket сервер запущен на ws://localhost:8765")
    # Блокируемся до закрытия сервера
    await server.wait_closed()


if __name__ == "__main__":
    asyncio.run(main())
