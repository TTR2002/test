<script setup lang="ts">
import { onMounted, ref } from 'vue'
import HelloOrigame from './components/HelloOrigame.vue'

const backVersion = ref<string>('…')

onMounted(async () => {
  try {
    const res = await fetch('/api/version')
    const data: { version: string } = await res.json()
    backVersion.value = data.version
  } catch {
    backVersion.value = 'back injoignable'
  }
})
</script>

<template>
  <main>
    <HelloOrigame name="Rodrigue" />
    <p>Version du back : <code>{{ backVersion }}</code></p>
  </main>
</template>
