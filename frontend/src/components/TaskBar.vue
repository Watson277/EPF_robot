<template>
    <div class="taskbar">
      <BatteryWidget />
      <Time />
    </div>

  </template>
  
  <script setup>
  import BatteryWidget from './BatteryWidget.vue'
  import Time from './Time.vue'
  </script>
  
  <style scoped>
  .taskbar {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 70px;
    background-color: #222;
    color: white;
    display: flex;
    align-items: center;
    padding: 0 20px;
    z-index: 9999;
    justify-content: space-between;
  }
  </style>
  