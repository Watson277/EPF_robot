<template>
  <div class="container">
    <h2 class="title">🎙️ Start the conversation</h2>
    <button @click="startRecording" :disabled="recording" class="btn">🎙️ Start</button>
    <button @click="stopRecording" :disabled="!recording" class="btn">⏹️ Stop</button>
    <div v-if="reply" class="reply">🤖 Reply: {{ reply }}</div>
  </div>
</template>

<script setup>
import { ref, onMounted, onBeforeUnmount } from 'vue'

const recording = ref(false)
const reply = ref('')
let mediaRecorder, audioChunks = []
// 连接 WebSocket
const ws = new WebSocket("ws://localhost:8765")

ws.onopen = () => {
  console.log("WebSocket connected")
}
ws.onmessage = (event) => {
  console.log("Message from server:", event.data)
}

const socket = ref<WebSocket | null>(null);

onBeforeUnmount(() => {
  try {
    if (socket.value && socket.value.readyState === WebSocket.OPEN) {
      socket.value.close();
    }
  } catch (error) {
    console.error("Error during socket cleanup:", error);
  }
});


const startRecording = async () => {
  const stream = await navigator.mediaDevices.getUserMedia({ audio: true })
  mediaRecorder = new MediaRecorder(stream)
  mediaRecorder.ondataavailable = e => audioChunks.push(e.data)
  mediaRecorder.onstop = sendAudio
  audioChunks = []
  mediaRecorder.start()
  recording.value = true
}

const stopRecording = () => {
  mediaRecorder.stop()
  recording.value = false
}

const speakText = (text) => {
  if ('speechSynthesis' in window) {
    const utterance = new SpeechSynthesisUtterance(text)
    utterance.lang = 'en-US'
    utterance.rate = 1
    utterance.pitch = 1
    speechSynthesis.speak(utterance)
  }
}

// 修改 sendAudio 函数，转录完成后通过 WebSocket 发文本
const sendAudio = async () => {
  const blob = new Blob(audioChunks, { type: 'audio/webm' })
  const formData = new FormData()
  formData.append('file', blob, 'audio.webm')

  const res = await fetch('http://localhost:8000/recognize', {
    method: 'POST',
    body: formData
  })
  const data = await res.json()
  reply.value = data.reply

  // 朗读
  speakText(data.reply)

  // 通过 WebSocket 发送转录文本给 server.py 处理
  if (ws.readyState === WebSocket.OPEN) {
    ws.send(JSON.stringify({ type: "text", content: data.text }))
  }
}


</script>

<style scoped>
.container {
  background-color: #0b1e3c; /* 深蓝背景 */
  min-height: 100vh;
  margin: 0;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  gap: 18px;
  color: white;
  font-family: Arial, sans-serif;
  text-align: center;
}

.title {
  margin: 0;
  font-size: 2rem;
}

.btn {
  background-color: #e60000; /* 红色按钮 */
  border: none;
  padding: 14px 38px;
  font-size: 1.5rem;
  font-weight: bold;
  color: white;
  border-radius: 8px;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.btn:disabled {
  background-color: #990000;
  cursor: not-allowed;
}

.btn:hover:not(:disabled) {
  background-color: #ff1a1a;
}

.reply {
  font-size: 1.2rem;
  max-width: 600px;
  text-align: center;
}
</style>
