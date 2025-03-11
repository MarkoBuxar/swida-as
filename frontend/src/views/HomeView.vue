<script setup lang="ts">
import { ref, onMounted } from 'vue'
import axios from 'axios'
import Orders from '@/components/Orders.vue'
import { apiBase } from '@/App.vue'

export interface Waypoint {
  address: string
  waypoint_type: "Delivery" | "Pickup"
}

export interface Order {
  order_number: number
  customer_name: number
  order_date: string
  waypoints: Waypoint[]
}


const orderList = ref([] as Order[])
const customerFilter = ref("")
let filterString = ""


const fetchOrders = async () => {
  const f = await axios.get<Order[]>(`${apiBase}/orders?${filterString}`)
  orderList.value.push(...f.data)
  fetchedData = orderList.value
}

const applyFilters = async () => {
  if (!customerFilter.value) filterString = ""
  filterString = `customer=${customerFilter.value}`


  orderList.value = [] as Order[]
  await fetchOrders()
}

onMounted(async () => {
  await fetchOrders()
})

</script>

<script lang="ts">
export let fetchedData = [] as Order[]

</script>

<template>
  <p>filter: </p> <input v-model=customerFilter placeholder="customer name" />
  <button @click=applyFilters>apply filter</button>


  <Orders :orders=orderList></Orders>
</template>
