import { createApp } from 'vue'
import App from './App.vue'
import './style.css'
import router from './router'
import i18n from './i18n'
import AOS from 'aos'
import 'aos/dist/aos.css'

const app = createApp(App)

app.use(router)
app.use(i18n)

// Initialize AOS
AOS.init({
  duration: 800,
  easing: 'ease-in-out',
  once: true,
  offset: 100
})

app.mount('#app')
