<script setup lang="ts">
import { ref } from 'vue'
import axios from 'axios'
import { apiBase } from '@/App.vue'
import router from '@/router'

const customerName = ref("")
const error_flag = ref(false)


const createOrder = async () => {
    const body = { customer: customerName.value }

    if (!body.customer) {
        error_flag.value = true
        return
    }
    await axios.post(`${apiBase}/orders/create`, body)
    router.push({ path: '/' })

}

</script>

<template>
    <h1>Create Order</h1>

    <input placeholder="customer name" v-model=customerName>

    <button @click=createOrder>create new order</button>

    <p v-if=error_flag>Customer name cannot be empty</p>

</template>