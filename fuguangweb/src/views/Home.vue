<script setup lang="ts">
import Header from "../components/Header.vue"
import Footer from "../components/Footer.vue"

// 测试CORS的跨域配置是否有问题
// import http from "../utils/http";

// 测试客户端的跨域是否配置成功
// http.get("/api/home/demo/").then(response=>{
//   console.log(response.data);
// })

// 测试服务端的跨域是否配置成功
// http.get("/home/demo/").then(response=>{
//   console.log(response.data);
// })
</script>

<template>
 <div class="home">
    <Header></Header>

    <Footer></Footer>
  </div>
</template>

<style scoped>

</style>