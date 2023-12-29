<script setup lang="ts">
import { ref } from "vue";
import { RewardTableViewType } from "../../../components/RewardTableViewType";
import RewardTableView from "../../../components/RewardTableView.vue";

const res_data = ref<RewardTableViewType>([]);

async function get_data() {
	const res = await fetch("http://localhost:8000/api/rewards");
	const data = await res.json();
	res_data.value = data;
}

await get_data();
</script>

<template>
	<RewardTableView :data="res_data" />
</template>
