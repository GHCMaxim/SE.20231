<script setup lang="ts">
import HouseholdMonthlyView from "../../../components/HouseholdMonthlyView.vue";
import { ref } from "vue";
import { HouseholdMonthlyViewType } from "../../../components/HouseholdMonthlyViewType";

const res_data = ref<HouseholdMonthlyViewType>([]);

async function get_data() {
	const res = await fetch(
		`http://localhost:8000/api/payments/monthly/household`,
	);
	const data = await res.json();
	res_data.value = data;
}

await get_data();
</script>
<template>
	<HouseholdMonthlyView :data="res_data" />
</template>
