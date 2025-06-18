<template>
  <div class="container">
    <h2 class="title">🎙️ Start the conversation</h2>
    <button @click="startRecording" :disabled="recording" class="btn">🎙️ Start</button>
    <button @click="stopRecording" :disabled="!recording" class="btn">⏹️ Stop</button>
    <div class="dialog-box">
      <div v-if="prompt" class="prompt">🧑 You: {{ prompt }}</div>
      <div v-if="reply" class="reply">🤖 Reply: {{ reply }}</div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';

const prompt = ref('');
const reply = ref('');

const fetchDialog = async () => {
  try {
    const res = await fetch('http://10.2.60.80:8000/latest');  // ⚠️ 请确保 IP 和端口正确
    const data = await res.json();
    prompt.value = data.prompt || '';
    reply.value = data.response || '';
  } catch (e) {
    console.error('❌ 获取对话失败：', e);
  }
};

onMounted(() => {
  fetchDialog(); // 初次加载
  setInterval(fetchDialog, 2000); // 每2秒刷新一次
});
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

.dialog-box {
  padding: 1.5rem;
  background-color: #f0f4f8;
  border-radius: 16px;
  max-width: 700px;
  margin: 2rem auto;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
  font-size: 1.4rem; /* ⬅️ 放大整体字体 */
  font-family: "Segoe UI", Tahoma, Geneva, Verdana, sans-serif;
  line-height: 1.6;
}

.prompt {
  color: #0056b3;
  margin-bottom: 1rem;
  font-weight: 600;
}

.reply {
  color: #0a7f49;
  font-weight: 500;
}
</style>
