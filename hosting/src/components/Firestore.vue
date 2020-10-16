<template>
 <div>
   <div>2{{User.depa}}{{User.num}}の正答数一覧</div>
   <li 
     v-for="post in posts"
     :key="post.id"
     class="list-none my-5"
   >
     <h2 class="text-xl">{{ post.score }}</h2>
     <p class="text-sm">{{ post.date }}</p>
   </li>
 </div>
</template>

<script>
import { db } from '@/main'
export default {
  props:{
    User: Object
  },
  data() {
    return {
      posts: []
    }
  },
  firestore() {
    return {
      posts: db.collection("2"+this.User.depa+this.User.num)
    }
  }
}
</script>