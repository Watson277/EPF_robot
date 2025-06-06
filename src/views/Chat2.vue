<template>
  <div class="wrapper">
    <AudioRecorder />
  </div>
</template>

<script setup>
import AudioRecorder from '../components/AudioRecorder.vue'
</script>

<style scoped>
.wrapper {
  background-color: #0b1e3c;  /* 深蓝背景 */
  min-height: 100vh;
  margin: 0;
  display: flex;
  flex-direction: column;
  justify-content: center;    /* 垂直居中 */
  align-items: center;        /* 水平居中 */
  gap: 12px;                  /* 控制标题和按钮间距 */
  color: white;
  font-family: Arial, sans-serif;
  text-align: center;
}


</style>
