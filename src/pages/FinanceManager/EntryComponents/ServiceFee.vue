<script setup lang="ts">
import RateTableView from "../../../components/RateTableView.vue";
import { ref } from "vue";
import { RateTableViewType } from "../../../components/RateTableViewType";

const res_data = ref<RateTableViewType>([]);

async function get_data() {
	const res = await fetch("http://localhost:8000/api/payments_types/3");
	const data = await res.json();
	res_data.value = data;
}
await get_data();
</script>

<template>
	<RateTableView :data="res_data" />
</template>
