#!/usr/bin/env python3
import asyncio
import websockets


async def client():
    uri = "ws://localhost:8765"
    # Открываем соединение
    async with websockets.connect(uri) as websocket:
        message = "Привет, сервер!"
        print(f"Отправка: {message}")
        await websocket.send(message)

        # Получаем и выводим ровно пять ответных сообщений
        for _ in range(5):
            response = await websocket.recv()
            print(f"Ответ от сервера: {response}")


if __name__ == "__main__":
    asyncio.run(client())
