<template>
	<Pie :data="data" :options="options" />
</template>

<script lang="ts">
import { Chart as ChartJS, ArcElement, Tooltip, Legend } from "chart.js";
import { Pie } from "vue-chartjs";
import { ref } from "vue";

ChartJS.register(ArcElement, Tooltip, Legend);

const res_data = ref([]);

async function get_data() {
	const res = await fetch("http://localhost:8000/api/statistics/age");
	const data = await res.json();
	res_data.value = data;
}

await get_data();

const data = {
	labels: ["0-10", "11-18", "19-30", "31-50", "51-70", "71+"],
	datasets: [
		{
			backgroundColor: [
				"#41B883",
				"#E46651",
				"#00D8FF",
				"#DD1B16",
				"#FFC700",
				"#FFC800",
			],
			data: res_data.value,
		},
	],
};

const options = {
	responsive: false,
	maintainAspectRatio: true,
};

export default {
	name: "App",
	components: {
		Pie,
	},
	data() {
		return {
			data,
			options,
		};
	},
};
</script>
