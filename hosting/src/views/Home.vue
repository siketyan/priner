<template>
 <div class="home">
   <h1>正答数一覧</h1>
   <li 
     v-for="post in posts"
     :key="post.id"
     class="list-none my-5"
   >
     <h2 class="text-xl">{{ post.title }}</h2>
     <p class="text-sm">{{ post.createAt }}</p>
   </li>
 </div>
</template>

<script>
import { db } from '@/main'
export default {
  name: 'home',
  data() {
    return {
      posts: []
    }
  },
  firestore() {
    return {
      posts: db.collection('posts')
    }
  }
}
</script>