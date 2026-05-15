import { defineConfig } from 'astro/config';

export default defineConfig({
  output: 'server',
  integrations: [],
  server: {
    port: 3000
  }
});