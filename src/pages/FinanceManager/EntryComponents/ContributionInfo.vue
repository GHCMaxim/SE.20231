<script setup lang="ts">
import { ref } from "vue";
import { ContributionsTableViewType } from "../../../components/ContributionsTableViewType";
import ContributionsTableView from "../../../components/ContributionsTableView.vue";
const res_data = ref<ContributionsTableViewType>([]);

async function get_data() {
	const res = await fetch("http://localhost:8000/api/contributions");
	const data = await res.json();
	res_data.value = data;
}

await get_data();
</script>

<template>
	<ContributionsTableView :data="res_data" />
</template>
