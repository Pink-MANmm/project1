import { createApp } from 'vue'
import App from './App.vue'
import router from './router'


// 引入 Echarts
import * as echarts from 'echarts';
// 引入词云外部插件
import 'echarts-wordcloud';

import axios from 'axios'

import '@/assets/bootstrap-theme.min.css'
import '@/index.css'

const app = createApp(App)

axios.defaults.baseURL = "http://127.0.0.1:5555/"
app.config.globalProperties.$http = axios
app.config.globalProperties.$echarts = echarts

app.use(router)
app.mount('#app')
