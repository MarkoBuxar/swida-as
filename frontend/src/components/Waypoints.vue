<script setup lang="ts">
import type { Waypoint } from '@/views/HomeView.vue';

defineProps<{ waypoints: Waypoint[] }>()
</script>

<template>
    <table class="waypoints">
        <tbody>
            <tr v-for="(waypoint, i) in waypoints" :key="i">
                <td>{{ waypoint.address }}</td>
                <td>{{ waypoint.waypoint_type }}</td>
            </tr>
        </tbody>
    </table>
</template>

<style scoped>
table,
th,
td {
    border: 0px solid;
}

table {
    border-bottom: 1px solid;
    border-top: 1px solid;
    width: 100%;
}
</style>