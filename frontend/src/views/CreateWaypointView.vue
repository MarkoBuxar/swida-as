<script setup lang="ts">
import { apiBase } from '@/App.vue';
import axios from 'axios';
import { fetchedData, type Order } from './HomeView.vue';
import { onMounted, ref } from 'vue';
import router from '@/router';

interface Option {
    text: string
    value: any
}

const orderList = ref([] as Option[])
const order = ref("")
const address = ref("")
const waypointType = ref("p")
let error_flag = ref(false)


const getOrderList = async () => {
    if (!fetchedData.length) {
        const f = await axios.get<Order[]>(`${apiBase}/orders`)
        fetchedData.push(...f.data)
    }


    fetchedData.forEach(o => {
        orderList.value.push({ text: `#${o.order_number} - ${o.customer_name}`, value: o.order_number })
    });

}

const createWaypoint = async () => {
    const body = { address: address.value, waypoint_type: waypointType.value }

    if (!body.address) {
        error_flag.value = true
        return
    }

    await axios.post(`${apiBase}/waypoints/${order.value}`, body)
    router.push({ path: '/' })
}

onMounted(async () => {
    await getOrderList()
})
</script>


<template>
    <h1>Create Waypoint</h1>


    <select v-model="order">
        <option v-for="option in orderList" :value="option.value">
            {{ option.text }}
        </option>
    </select>



    <div v-if=order>

        <p>New waypoint: </p>

        <input placeholder="address" v-model=address>

        <select v-model="waypointType" placeholder="type">
            <option value="p">Pickup</option>
            <option value="d">Delivery</option>
        </select>

        <button @click=createWaypoint>create new waypoint</button>

        <p v-if=error_flag>Address cannot be empty</p>

    </div>
</template>