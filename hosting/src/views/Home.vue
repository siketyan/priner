<template>
  <div id="home">
    <Firestore :User="user" />
  </div>
</template>

<script>
  import Firestore from '@/components/Firestore'
  export default {
    components: {
      Firestore
    },
    data(){
      return{
       user: {
         depa: "i",
         num: "38"
       },
      }
    }
  }
</script>>