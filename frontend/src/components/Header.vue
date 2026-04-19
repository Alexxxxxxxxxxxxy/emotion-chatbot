<script setup lang="ts">
</script>

<template>
    <!-- 把 pt-5 改成 p-5（全方向内边距，效果明显），加大到 p-6 更直观 -->
    <div class="flex flex-row justify-between align-center bg-blue-400 w-full px-4 py-2 rounded-md">
        <div class="text-white hover:cursor-pointer">Alex.ai</div>
        <div class="flex flex-row gap-3.5">
            <span class="text-white hover:border-b-2 hover:cursor-pointer">情绪聊天</span>
            <span class="text-white hover:border-b-2 hover:cursor-pointer">文件总结</span>
        </div>
        
        <button class="bg-black px-2 py-1 text-white rounded-md hover:cursor-pointer hover:bg-gray-700 active:bg-gray-950">登录/注册</button>
    
    </div>
</template>