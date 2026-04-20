<script setup lang="ts">
import { ref } from 'vue';

const props = defineProps<{
    show: boolean
}>()
const emit = defineEmits<{
    toggle: [visible: boolean]
}>()
const isLogin = ref(true)

const username = ref("")
const password = ref("")
const email = ref("")

const onClick = () => {
    emit("toggle", false)
}

const ToggleStatus = () => {
    isLogin.value = !isLogin.value
}

const handleSubmit = (e: Event) => {
    e.preventDefault()
    // 后续在这里写登录/注册逻辑
    console.log('提交', { username: username.value, password: password.value, email: email.value })
}
</script>

<template>
    <div 
        class="fixed inset-0 z-50 flex items-center justify-center bg-black/60 backdrop-blur-sm transition-opacity duration-300"
        :class="props.show ? 'opacity-100' : 'opacity-0 pointer-events-none'"
        @click.self="onClick"
    >
        <div 
            class="w-full max-w-md bg-white rounded-2xl shadow-2xl overflow-hidden transform transition-all duration-300"
            :class="props.show ? 'scale-100' : 'scale-95'"
        >
            <div class="flex justify-end p-4">
                <button 
                    class="w-8 h-8 flex items-center justify-center rounded-full text-gray-400 hover:bg-gray-100 hover:text-gray-600 transition-colors hover:cursor-pointer"
                    @click="onClick"
                >
                    ✕
                </button>
            </div>

            <div class="px-8 pb-10">
                <h2 class="text-center text-3xl font-bold text-gray-800 mb-8">
                    {{ isLogin ? '欢迎回来' : '创建账号' }}
                </h2>

                <form 
                    class="space-y-5"
                    @submit.prevent="handleSubmit"
                >
                    <div>
                        <label for="username" class="block text-sm font-medium text-gray-700 mb-1.5">
                            用户名
                        </label>
                        <input 
                            type="text" 
                            id="username" 
                            v-model="username" 
                            required
                            class="w-full px-4 py-2.5 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500 outline-none transition-all"
                            placeholder="请输入用户名"
                        >
                    </div>

                    <div>
                        <label for="password" class="block text-sm font-medium text-gray-700 mb-1.5">
                            密码
                        </label>
                        <input 
                            type="password" 
                            id="password" 
                            v-model="password" 
                            required
                            class="w-full px-4 py-2.5 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500 outline-none transition-all"
                            placeholder="请输入密码"
                        >
                    </div>

                    <div v-if="!isLogin">
                        <label for="email" class="block text-sm font-medium text-gray-700 mb-1.5">
                            邮箱
                        </label>
                        <input 
                            type="email" 
                            id="email" 
                            v-model="email" 
                            required
                            class="w-full px-4 py-2.5 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500 outline-none transition-all"
                            placeholder="请输入邮箱地址"
                        >
                    </div>

                    <button 
                        type="submit"
                        class="w-full py-3 bg-blue-600 text-white font-medium rounded-lg hover:bg-blue-700 active:bg-blue-800 transition-colors shadow-md hover:shadow-lg hover:cursor-pointer"
                    >
                        {{ isLogin ? '登录' : '注册' }}
                    </button>
                </form>

                <div class="mt-8 text-center text-sm text-gray-600">
                    <span v-if="isLogin">
                        还没有账号？
                        <span 
                            class="text-blue-600 font-medium hover:text-blue-700 underline cursor-pointer transition-colors"
                            @click.stop.prevent="ToggleStatus"
                        >
                            立即注册
                        </span>
                    </span>
                    <span v-else>
                        已有账号？
                        <span 
                            class="text-blue-600 font-medium hover:text-blue-700 underline cursor-pointer transition-colors"
                            @click.stop.prevent="ToggleStatus"
                        >
                            立即登录
                        </span>
                    </span>
                </div>
            </div>
        </div>
    </div>
</template>