<script setup lang="ts">
import { ref } from 'vue';
import axios from 'axios';

const answer = ref('🤖: 你好呀，我是一个情感聊天机器人，你有什么需要帮助的吗？');
const input = ref('');

const sendMessage = async () =>{
    await axios.post(
        'http://127.0.0.1:8080/chat',
        {
            session_id:"2",
            query:`${input.value}`
        }
    ).then(res=>{
        console.log(res)
        answer.value = res.data.response;
        input.value = '';
    }).catch(err=>{
        answer.value = '网络错误，请稍后重试,'+err;
    })
}

</script>

<template>
  <div class="h-full flex flex-col relative w-full max-w-3xl mx-auto bg-white rounded-2xl shadow-xl overflow-hidden">
    
    <div class="flex-1 overflow-y-auto p-6 scrollbar-hide bg-linear-to-b from-gray-50 to-white flex flex-col justify-start">
      <div class="bg-blue-50 text-blue-800 px-5 py-3 rounded-2xl rounded-tl-none max-w-[80%] shadow-sm">
        <span class="whitespace-pre-line">{{ answer }}</span>
      </div>
    </div>

    <!-- 输入区域：优化布局、间距和样式 -->
    <div class="flex flex-row items-center gap-3 w-full p-4 bg-white border-t border-gray-100">
      <input 
        type="text" 
        v-model="input" 
        class="flex-1 border-2 border-gray-200 rounded-xl px-4 py-3 focus:ring-2 focus:ring-blue-500 focus:border-blue-500 outline-none transition-all"
        placeholder="输入你想说的话..."
        @keypress.enter="sendMessage"
      >
      <button 
        @click="sendMessage" 
        class="bg-linear-to-r from-blue-500 to-blue-600 px-6 py-3 text-white rounded-xl hover:from-blue-600 hover:to-blue-700 active:from-blue-700 active:to-blue-800 cursor-pointer transition-all duration-200 shadow-md hover:shadow-lg font-medium"
      >
        发送
      </button>
    </div>
  </div>
</template>

<style scoped>
.scrollbar-hide::-webkit-scrollbar {
  display: none;
}
.scrollbar-hide {
  -ms-overflow-style: none;
  scrollbar-width: none;
}
</style>