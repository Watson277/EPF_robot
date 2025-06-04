<template>
    <div class="home">
      <h1>Welcome to <span class="highlight">EPF</span></h1>
      <button @click="goToChat">Start</button>
      <button @click="goToChat2">Speak with me</button>
    </div>
  </template>
  
  <script setup>
  import { useRouter } from 'vue-router'
  const router = useRouter()
  
  function goToChat() {
    router.push('/chat')
  }
  function goToChat2() {
    router.push('/chat2')
  }
  </script>
  
  <style scoped>
  .home {
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
  
  .highlight {
    color: #e63946; /* 深红色标题强调 */
  }
  
  button {
    background-color: #e63946;
    color: white;
    padding: 14px 26px;
    font-size: 20px;
    border: none;
    border-radius: 8px;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.3);
    cursor: pointer;
    transition: background 0.3s ease;
    margin-top: 20px;
  }
  
  button:hover {
    background-color: #c72c3a;
  }
  </style>
  