<script setup lang="ts">

const emit = defineEmits<{
    show:[status:boolean]
}>()
const onClick = ()=>{
    emit("show",true)
}

</script>

<template>
    <div class="flex flex-row justify-between items-center bg-linear-to-r from-blue-500 to-blue-600 w-full px-6 py-3 rounded-xl shadow-lg">
        <div class="text-white font-bold text-xl hover:opacity-90 cursor-pointer transition-opacity">
            Alex.ai
        </div>
        <div class="flex flex-row gap-6">
            <span class="text-white/90 hover:text-white hover:border-b-2 border-white/80 px-1 py-0.5 cursor-pointer transition-all duration-200 font-medium">
                情绪聊天
            </span>
            <span class="text-white/90 hover:text-white hover:border-b-2 border-white/80 px-1 py-0.5 cursor-pointer transition-all duration-200 font-medium">
                文件总结
            </span>
        </div>
        <button 
            class="bg-black/80 hover:bg-black/90 active:bg-black px-5 py-2 text-white rounded-lg cursor-pointer transition-all duration-200 shadow-md hover:shadow-lg font-medium"
            @click="onClick"
        >
            登录/注册
        </button>
    </div>
</template>