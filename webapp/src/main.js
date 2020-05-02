import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import VueNativeSock from 'vue-native-websocket';
import AxiosDjango from '@/plugins/AxiosDjango';

import { library } from '@fortawesome/fontawesome-svg-core'
import { far } from '@fortawesome/free-regular-svg-icons'
import { fas } from '@fortawesome/free-solid-svg-icons'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'

library.add(far)
library.add(fas)

Vue.component('font-awesome-icon', FontAwesomeIcon)


Vue.use(AxiosDjango)

const socket = process.env.NODE_ENV === 'production' ? "wss://lesgens.co" : 'ws://localhost:8000'
Vue.use(VueNativeSock, socket, {
  store: store,
  format: 'json',
  reconnection: true, // (Boolean) whether to reconnect automatically (false)
  //reconnectionAttempts: 5, // (Number) number of reconnection attempts before giving up (Infinity),
  reconnectionDelay: 3000 // (Number) how long to initially wait before attempting a new (1000)
});


new Vue({
  router,
  store,
  render: h => h(App),
}).$mount('#app')
