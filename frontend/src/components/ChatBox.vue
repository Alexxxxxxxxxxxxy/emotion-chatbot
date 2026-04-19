<script setup lang="ts">
import { ref } from 'vue';
import axios from 'axios';

const answer = ref('你好呀，我是一个情感聊天机器人，你有什么需要帮助的吗？');
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
        answer.value = '网络错误，请稍后重试'+err;
    })
}

const handlechange = (e: Event) => {
    input.value = (e.target as HTMLInputElement).value;
}
</script>

<template>
  <!-- 🔥 根容器：包所有内容，占满全屏，弹性布局 -->
  <div class="flex flex-col min-h-screen relative">
    <!-- 🔥 聊天区域：flex-1 占满剩余高度 + 隐藏滚动条 -->
    <div class="flex-1 overflow-y-auto p-5 scrollbar-hide">
      <span>{{ answer }}</span>
    </div>

    <!-- 底部输入框（fixed 定位） -->
    <div class="flex flex-row items-center gap-2 fixed w-[95vw] bottom-0 left-1/2 -translate-x-1/2 mb-3">
      <input 
        type="text" 
        v-model="input" 
        class="flex-1 border-2 rounded-md p-2"
        @change="handlechange"
      >
      <button @click="sendMessage" class="bg-black px-4 py-2 text-white rounded-md hover:bg-gray-700 active:bg-gray-950 hover:cursor-pointer">
        发送
      </button>
    </div>
  </div>
</template>

<!-- 🔥 兼容全浏览器隐藏滚动条（备用样式，确保100%隐藏） -->
<style scoped>
.scrollbar-hide::-webkit-scrollbar {
  display: none;
}
.scrollbar-hide {
  -ms-overflow-style: none;
  scrollbar-width: none;
}
</style>