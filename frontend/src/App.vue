<template>
  <div id="app">
    <TaskBar />
    <div class="page-content">
      <router-view />
    </div>
  </div>
</template>

<script setup>
import AudioRecorder from './components/AudioRecorder.vue'
import TaskBar from './components/TaskBar.vue'
</script>

<style>
body {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  margin: 0;
  padding: 0;
  overflow: hidden;
}

#app {
  padding-top: 0px; /* 给任务栏高度留空间 */
  min-height: 100vh;
}

.page-content {
  padding: 0px;
}
</style>