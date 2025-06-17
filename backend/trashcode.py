import requests

# # Ollama API 地址（已绑定到你的 Windows 主机 IP）
# OLLAMA_URL = "http://10.2.60.55:11434/api/generate"

# # 输入你的 prompt 和模型名称
# prompt = "hello"
# model_name = "phi"  # 改成你实际 pull 的模型，如：llama3、mistral、gemma 等

# # 构造请求数据
# payload = {
#     "model": model_name,
#     "prompt": prompt,
#     "stream": False  # 如果需要流式输出改为 True
# }

# # 发送 POST 请求
# response = requests.post(OLLAMA_URL, json=payload)

# # 解析并打印结果
# if response.status_code == 200:
#     result = response.json()
#     print("模型回复：", result["response"])
# else:
#     print("请求失败，状态码：", response.status_code)
#     print(response.text)

response = requests.get("http://10.2.60.163:8000/reponse", params={"prompt": "What is EPF"})
result = response.json()
print("Model responsed: ", result)