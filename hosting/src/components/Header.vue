<template>
 <header class="fixed top-0 w-full p-3">
   <div class="flex justify-between">
     <router-link to="/">
       <h1 class="text-3xl font-bold">Priner</h1>
     </router-link>
     <div class="flex">
       <div class="w-10 h-10 rounded-full bg-black mr-2"></div>
       <div>
         <p>User</p>
         <p class="-mt-1 text-sm"><router-link to="/login">Log Out</router-link></p>
       </div>
     </div>
   </div>
 </header>
</template>