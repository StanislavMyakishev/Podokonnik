import Vue from 'vue'
import App from './App.vue'
import router from './router'
import Vuetify from 'vuetify'
import 'vuetify/dist/vuetify.min.css'
import "vue-material-design-icons/styles.css"
import 'material-design-icons-iconfont/dist/material-design-icons.css' // Ensure you are using css-loader

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