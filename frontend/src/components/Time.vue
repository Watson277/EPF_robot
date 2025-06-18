<template>
    <div class="time-display">
      📅 {{ currentTime }}
    </div>
  </template>
  
  <script setup>
  import { ref, onMounted } from 'vue'
  
  const currentTime = ref('')
  
  async function fetchTime() {
    try {
      const res = await fetch('http://localhost:8000/time')  // 替换成你自己的 IP
      const data = await res.json()
      currentTime.value = data.time
    } catch (e) {
      currentTime.value = 'Cannot obtain time information'
    }
  }
  
  onMounted(() => {
    fetchTime()
    setInterval(fetchTime, 1000)  // 每秒更新
  })
  </script>
  
  <style scoped>
  .time-display {
    font-size: 14px;
    color: #fff;
    width: 200px;
  }
  </style>
  
