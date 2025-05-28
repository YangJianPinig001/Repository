<script setup lang="ts">

const button_click = () => {
  alert('Button clicked!');
};
</script>

<template>
  <div class="test">test app main</div>
  <!-- vue 绑定按钮 -->
   <button @click="button_click">Click Me</button>
</template>

<style scoped>
.test {
  color: red;
  font-size: 20px;
  width: 100px;
  height: 100px;
}
</style>
