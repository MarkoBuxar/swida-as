<script setup lang="ts">
import { RouterLink, RouterView } from 'vue-router'


</script>

<script lang="ts">
export const apiBase = "http://localhost:3500/logistics"

</script>

<template>
  <header>
    <nav>
      <RouterLink to="/">Home</RouterLink>
      <RouterLink to="/order">Create Order</RouterLink>
      <RouterLink to="/waypoint">Create Waypoint</RouterLink>
    </nav>
  </header>

  <RouterView />
</template>

<style scoped></style>
