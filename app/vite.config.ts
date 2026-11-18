import { defineConfig } from 'vitest/config'
import vue from '@vitejs/plugin-vue'

export default defineConfig({
  plugins: [vue()],
  server: {
    // En local : les appels /api partent vers le back (mvn spring-boot:run)
    proxy: { '/api': 'http://localhost:8080' },
  },
  test: {
    environment: 'jsdom',
  },
})
