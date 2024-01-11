<script setup lang="ts">
import EssentialFeeView from "../../../components/EssentialFeeView.vue";
import { ref } from "vue";
import { EssentialsFeeViewType } from "../../../components/EssentialsFeeViewType";

const res_data = ref<EssentialsFeeViewType>([]);

async function get_data() {
	const res = await fetch(
		"http://localhost:8000/api/payments/monthly/service",
	);
	const data = await res.json();
	res_data.value = data;
}
await get_data();
</script>

<template>
	<EssentialFeeView :data="res_data" />
</template>
