<script setup lang="ts">
const props = defineProps<{ name: string }>()
</script>

<template>
  <h1>Bonjour {{ props.name }}, bienvenue sur mini OrigaMe</h1>
</template>
