<script setup lang="ts">
import { ref } from "vue";
import { VehicleCountViewType } from "../../../components/VehicleCountViewType";
import VehicleCountView from "../../../components/VehicleCountView.vue";

const res_data = ref<VehicleCountViewType>([]);

async function get_data() {
	const res = await fetch(
		"http://localhost:8000/api/payments/monthly/vehicle",
	);
	const data = await res.json();
	res_data.value = data;
}
await get_data();
</script>

<template>
	<VehicleCountView :data="res_data" />
</template>
