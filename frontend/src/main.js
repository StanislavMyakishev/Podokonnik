import Vue from 'vue'
import App from './App.vue'
import router from './router'
import Vuetify from 'vuetify'
import 'vuetify/dist/vuetify.min.css'

Vue.use(Vuetify, {
  theme: {
    primary: '#03A9F4',
    secondary: '#0288D1',
    accent: '#ff5722',
    error: '#B0002b',
    warning: '#FF6D00',
    info: '#ff9800',
    success: '#80CBC4'
  }
});

Vue.config.productionTip = false;

new Vue({
  render: h => h(App),
  router
}).$mount('#app');