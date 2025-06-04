import asyncio
from server import handle_message  # 假设你的 handle_message 在 websocket_server.py

async def process_voice_text(user_text: str):
    # 构造模拟消息（前端格式）
    fake_message = json.dumps({
        "type": "text",
        "content": user_text
    })
    
    # 调用已有的 WebSocket 消息处理逻辑
    await handle_message(fake_message)
