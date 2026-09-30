<template>
  <div id="app">
    <WelcomePopup v-if="showWelcome" @close="handleClose" />
    <router-view />
  </div>
</template>

<script>
import WelcomePopup from './components/WelcomePopup.vue';

export default {
  name: 'App',
  components: { WelcomePopup },
  data() {
    return {
      showWelcome: false
    };
  },
  created() {
    const dismissed = sessionStorage.getItem('welcomeDismissed');
    this.showWelcome = !dismissed;
  },
  methods: {
    handleClose() {
      this.showWelcome = false;
      sessionStorage.setItem('welcomeDismissed', 'true');
    }
  }
};
</script>

<style>
/* Global styles can be added here */
</style>