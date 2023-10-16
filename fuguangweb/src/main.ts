import {createApp} from 'vue'
import './style.css'
import App from './App.vue'
import router from './router'
import 'element-plus/dist/index.css'
import {createPinia} from 'pinia'
import store from "./store"


const app = createApp(App)

app.use(createPinia())
app.use(router)
app.use(store)
app.mount('#app')