import Vue from 'vue'
import App from './App.vue'
import './registerServiceWorker'
import router from './router'
import '@/assets/css/tailwind.css'

import { firestorePlugin } from 'vuefire'
import firebase from 'firebase'     
import 'firebase/firestore'

Vue.use(firestorePlugin)
firebase.initializeApp({
  apiKey: process.env.VUE_APP_FIREBASE_API_KEY,
  authDomain: process.env.VUE_APP_FIREBASE_AUTH_DOMAIN,
  databaseURL: process.env.VUE_APP_FIREBASE_DATABASE_URL,
  projectId: process.env.VUE_APP_FIREBASE_PROJECT_ID,
  storageBucket: process.env.VUE_APP_FIREBASE_STORAGE_BUCKET,
  messagingSenderId: process.env.VUE_APP_FIREBASE_MESSAGING_SENDER_ID
});

export const db = firebase.firestore()
export const auth = firebase.auth()

Vue.config.productionTip = false

new Vue({
  router,
  render: h => h(App)
}).$mount('#app')