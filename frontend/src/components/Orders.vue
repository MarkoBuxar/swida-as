<script setup lang="ts">
import type { Order } from '@/views/HomeView.vue';
import Waypoints from './Waypoints.vue';
import moment from 'moment';

defineProps<{ orders: Order[] }>()
</script>

<template>
  <table>
    <thead>
      <tr>
        <th>order number</th>
        <th>customer</th>
        <th>date</th>
        <th>waypoints</th>
      </tr>
    </thead>
    <tbody>
      <tr v-for="(order, i) in orders" :key="i">
        <td>{{ order.order_number }}</td>
        <td>{{ order.customer_name }}</td>
        <td>{{ moment(order.order_date).format('MMMM Do YYYY') }}</td>
        <Waypoints v-if="order.waypoints.length > 0" :waypoints=order.waypoints></Waypoints>
      </tr>
    </tbody>
  </table>
</template>
