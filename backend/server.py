import asyncio
import json
import websockets
from utils.command_parser import parse_command # 假设你有个解析函数

connected_clients = set()

async def handle_message(message):
    """
    处理从客户端来的消息，消息应为 JSON 格式
    """
    data = json.loads(message)
    user_text = data.get("content")
    print(f"[WebSocket] Received text: {user_text}")

    # 调用指令解析器解析文本
    command = parse_command(message)  # 解析出控制机器人动作的命令
    if command:
        print(f"[WebSocket] Parsed command: {command}")
        # execute_command(command)  # 执行机器人动作
        pass
    else:
        print("[WebSocket] No valid command found.")


async def handler(websocket):
    # 新客户端连接，加入集合
    connected_clients.add(websocket)
    try:
        async for message in websocket:
            await handle_message(message)
    except websockets.exceptions.ConnectionClosed:
        print("[WebSocket] Connection closed")
    finally:
        connected_clients.remove(websocket)



async def main():
    async with websockets.serve(handler, "0.0.0.0", 8765):
        print("[WebSocket] Server started at ws://0.0.0.0:8765")
        await asyncio.Future()  # 保持运行
