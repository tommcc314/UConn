import './assets/main.css'

import { createApp } from 'vue'
import App from './App.vue'
import { plugin, defaultConfig } from '@formkit/vue'
import { createAuth0 } from '@auth0/auth0-vue';
// Create the Vue app instance
const app = createApp(App)

// Use FormKit plugin
app.use(plugin, defaultConfig)
app.use(
    createAuth0({
      domain: import.meta.env.VITE_AUTH0_DOMAIN,
      clientId: import.meta.env.VITE_AUTH0_CLIENT_ID,
      authorizationParams: {
        redirect_uri: window.location.origin
      }
    })
  );

// Mount the app
app.mount('#app')
