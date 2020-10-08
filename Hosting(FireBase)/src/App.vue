<template>
  <div id="app">

    <Header />
    <main class="my-16 mx-auto">
      <router-view/>
    </main>
  </div>
</template>

<script>
  import Header from '@/components/Header'
  export default {
    components: {
      Header
    }
  }
</script>>

<style lang="stylus">
#app
  font-family Avenir, Helvetica, Arial, sans-serif
  -webkit-font-smoothing antialiased
  -moz-osx-font-smoothing grayscale
  text-align center
  color #2c3e50
  margin-top 60px
</style>
