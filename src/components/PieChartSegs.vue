<template>
	<Pie :data="data" :options="options" />
</template>

<script lang="ts">
import { Chart as ChartJS, ArcElement, Tooltip, Legend } from "chart.js";
import { Pie } from "vue-chartjs";
import { ref } from "vue";

const res_data = ref([]);

async function get_data() {
	const res = await fetch("http://localhost:8000/api/statistics/gender");
	const data = await res.json();
	res_data.value = data;
}

await get_data();

ChartJS.register(ArcElement, Tooltip, Legend);

const data = {
	labels: ["M", "F"],
	datasets: [
		{
			backgroundColor: [
				"#41B883",
				"#E46651",
				"#00D8FF",
				"#DD1B16",
				"#FFCE56",
				"#8A2BE2",
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
