<template>
    <div class="chat">
      <h2>AI ROBOT</h2>
      <textarea v-model="userMessage" placeholder="Please input your question..."></textarea>
      <br />
      <button @click="sendMessage" :disabled="loading">
        {{ loading ? "Sending..." : "Send" }}
      </button>
  

      <div class="response" v-if="aiResponse">
        <h3>AI Response: </h3>
        <p>{{ aiResponse }}</p>
      </div>
  
      <br />
      <button class="back-btn" @click="goHome">Return to homepage</button>
    </div>
  </template>
  
  <script setup>
import { ref } from 'vue'
const userMessage = ref('')
const aiResponse = ref('')
const loading = ref(false)
import { useRouter } from 'vue-router'
const router = useRouter()

function goHome() {
  router.push('/')
}

const ws = new WebSocket("ws://localhost:8765")
ws.onopen = () => {
  console.log("WebSocket connected")
}
ws.onmessage = (event) => {
  console.log("Message from server:", event.data)
}

// ws.onopen = () => {
//   ws.send(JSON.stringify({ type: 'text', content: 'move forward' }))
// }

async function sendMessage() {
  console.log("1")

  ws.send(JSON.stringify({ type: 'text', content: userMessage.value }))

  if (!userMessage.value.trim()) return

  loading.value = true
  aiResponse.value = ''
  
  // try {
    // const res = await fetch("http://10.2.60.55:11434/api/generate", {
    //   method: 'POST',
    //   headers: {
    //     'Content-Type': 'application/json'
    //   },
    //   body: JSON.stringify({
    //       model: "phi",
    //       prompt: userMessage.value,
    //       stream: false,
    //     }),
    // })
    try {
        const url = `http://10.2.60.163:8000/reponse?prompt=${encodeURIComponent(userMessage.value)}`
        const res = await fetch(url)
        
        if (!res.ok) {
          throw new Error(`HTTP 错误：${res.status}`)
        }

        aiResponse.value = await res.text()  // 注意这里是 text()，不是 json()

        // const data = await res.json()
        // aiResponse.value = data.response || 'AI 无响应'
    
  } catch (error) {
    console.error(error)
    aiResponse.value = '请求失败，请检查 LM Studio 是否正在运行'
    
  } finally {
    loading.value = false
  }


}



</script>

  
  
  <style scoped>
  .chat {
    background-color: #0b1e3c;  /* 深蓝背景 */
    min-height: 100vh;
    margin: 0;
    display: flex;
    flex-direction: column;
    justify-content: center;    /* 垂直居中 */
    align-items: center;        /* 水平居中 */
    gap: 10px;                  /* 控制标题和按钮间距 */
    color: white;
    font-family: Arial, sans-serif;
    text-align: center;
  }
  
  textarea {
    width: 50%;
    height: 120px;
    padding: 12px;
    font-size: 16px;
    border: 2px solid #e63946;
    border-radius: 8px;
    resize: none;
    margin-top: 20px;
    background: #fefefe;
    color: #333;
  }
  
  button {
    margin-top: 16px;
    padding: 11px 25px;
    font-size: 17px;
    background-color: #e63946;
    border: none;
    color: white;
    border-radius: 8px;
    cursor: pointer;
    box-shadow: 0 4px 10px rgba(0, 0, 0, 0.3);
    transition: background 0.3s;
  }
  
  button:hover {
    background-color: #c72c3a;
  }
  
  .response {
    margin-top: 30px;
    background: #142a4f; /* 更深的蓝 */
    padding: 20px;
    border-radius: 10px;
    width: 50%;
  }
  
  .back-btn {
    background-color: transparent;
    border: 1px solid #e63946;
    color: #e63946;
    margin-top: 30px;
  }
  
  .back-btn:hover {
    background-color: #e63946;
    color: white;
  }
  </style>
  