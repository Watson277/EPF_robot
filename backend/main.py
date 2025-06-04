import threading
import time
import asyncio
import uvicorn

from fastapi import FastAPI, WebSocket
from fastapi.middleware.cors import CORSMiddleware

from api.recognize_api import router as recognize_router
from control import movement, button, adc
import server  # 引用你写的 WebSocket 服务模块（server.py）

app = FastAPI()

# 配置跨域
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], allow_credentials=True,
    allow_methods=["*"], allow_headers=["*"]
)

# 挂载 API 路由
app.include_router(recognize_router)

# WebSocket 端点（可以删去，改由 server.py 管理）
@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        await websocket.send_text(f"Echo: {data}")

# 后台线程：运动控制
def run_movement_loop():
    while True:
        movement.check_and_move()
        time.sleep(0.1)

# 后台线程：按钮监听
def run_button_loop():
    while True:
        button.listen_buttons()
        time.sleep(0.1)

# 后台线程：电池电量检测
def run_adc_loop():
    while True:
        adc.read_battery()
        time.sleep(5)

# 🧠 运行 WebSocket 服务
def run_websocket_server():
    asyncio.run(server.main())  # 注意 server.py 中要定义 main() 协程

# 🚀 主函数
if __name__ == "__main__":
    # 启动控制模块线程
    threading.Thread(target=run_movement_loop, daemon=True).start()
    threading.Thread(target=run_button_loop, daemon=True).start()
    # threading.Thread(target=run_adc_loop, daemon=True).start()

    # 启动 WebSocket 服务线程
    threading.Thread(target=run_websocket_server, daemon=True).start()

    # 启动 FastAPI HTTP 服务（主线程）
    uvicorn.run(app, host="0.0.0.0", port=8000)
