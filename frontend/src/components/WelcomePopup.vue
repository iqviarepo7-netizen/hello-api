<template>
  <div class="welcome-popup overlay">
    <div class="popup-content">
      <h2>Welcome!</h2>
      <p>We're glad to have you here.</p>
      <button @click="close">Close</button>
    </div>
  </div>
</template>

<script>
export default {
  name: 'WelcomePopup',
  methods: {
    close() {
      this.$emit('close');
    }
  }
};
</script>

<style scoped>
.welcome-popup {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
  background: rgba(0, 0, 0, 0.5);
  z-index: 1000;
}
.popup-content {
  background: white;
  padding: 20px;
  border-radius: 8px;
  text-align: center;
}
button {
  margin-top: 10px;
}
</style>