<script setup lang="ts">
  import { RouterLink, RouterView } from 'vue-router'
  import { ref } from 'vue'

  import NavBar from './components/NavBar.vue'
  import "./App.css"
</script>

<template>
  <NavBar/>
  <RouterView />
</template>

<style>
@import url('https://fonts.googleapis.com/css?family=Inter');
</style>
