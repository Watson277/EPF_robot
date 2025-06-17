<template>
    <div class="battery-container">
      <div class="battery">
        <div class="battery-level" :style="levelStyle"></div>
      </div>
      <div class="battery-info">
        🔋 {{ percent }}%
      </div>
    </div>
  </template>
  
  <script setup>
  import { ref, onMounted, computed } from 'vue';
  
  const percent = ref(0);
  const voltage = ref('--');
  
  // 注意替换为你树莓派的实际 IP 地址或域名
  const apiUrl = 'http://<树莓派IP>:5000/battery';
  
  const fetchBattery = async () => {
    try {
      const res = await fetch(apiUrl);
      const data = await res.json();
      percent.value = data.percentage;
      voltage.value = data.voltage.toFixed(2);
    } catch (err) {
      console.error('获取电池信息失败:', err);
    }
  };
  
  const levelStyle = computed(() => ({
    width: `${percent.value}%`,
    backgroundColor:
      percent.value > 60 ? '#4caf50' :
      percent.value > 30 ? '#ff9800' : '#f44336'
  }));
  
  onMounted(() => {
    fetchBattery();
    setInterval(fetchBattery, 5000);
  });
  </script>
  
  <style scoped>
  .battery-container {
    font-family: sans-serif;
    display: flex; 
    margin: 20px;
    width: 120px;
    height: 60px;
    gap: 30px;
  }
  
  .battery {
    width: 100px;
    height: 40px;
    border: 2px solid #333;
    border-radius: 5px;
    position: relative;
    box-sizing: border-box;
    background-color: #eee;
  }
  
  .battery::after {
    content: "";
    position: absolute;
    right: -8px;
    top: 12px;
    width: 6px;
    height: 16px;
    background: #333;
    border-radius: 2px;
  }
  
  .battery-level {
    height: 100%;
    transition: width 0.5s ease;
    border-radius: 3px 0 0 3px;
    gap: 60px;
  }
  
  .battery-info {
    margin-top: 10px;
    font-size: 14px;
  }
  </style>
  