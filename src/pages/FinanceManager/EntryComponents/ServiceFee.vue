<script setup lang="ts">
import ServiceFeeView from "../../../components/ServiceFeeView.vue";
import { ref } from "vue";
import { ServiceFeeViewType } from "../../../components/ServiceFeeViewType";

const res_data = ref<ServiceFeeViewType>([]);

async function get_data() {
	const res = await fetch("http://localhost:8000/api/payments/monthly/house");
	const data = await res.json();
	res_data.value = data;
}
await get_data();
</script>

<template>
	<ServiceFeeView :data="res_data" />
</template>
