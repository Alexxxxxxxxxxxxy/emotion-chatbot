<script setup lang="ts">
import { ref } from 'vue';

import Header from './components/Header.vue';
import ChatBox from './components/ChatBox.vue';
import Login from './components/Login.vue';
// import Conversation from './components/Conversation.vue';


const showbox = ref(false)
const callBack = (status: boolean)=>{
  showbox.value = status
}
const callBackLogin = (visible: boolean)=>{
  showbox.value = visible
}
</script>

<template>
  <div class="h-screen flex flex-col box-border mx-5 items-center">
    <Login :show="showbox" @toggle="callBackLogin"/>
    <Header @show="callBack"/>
    <ChatBox class="flex-1"/>
  </div>
</template>