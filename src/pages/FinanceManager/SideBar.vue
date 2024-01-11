<script setup lang="ts">
import SidebarEntry from "../../components/SidebarEntry.vue";
import FinanceEntryType from "./entries";
import { ref } from "vue";

const output = ref("")
async function make_payments() {
	const res = await fetch("http://localhost:8000/api/payments/monthly/create");
	if (!res.ok) {
		output.value = res.statusText
		return
	}
	const data = await res.json();
	output.value = data;
}

defineProps({
	currentEntry: {
		type: String,
		required: true,
	},
});

defineEmits(["update:currentEntry"]);

const entriesTop = [
	FinanceEntryType.ParkingFee,
	FinanceEntryType.BillEssentials,
	FinanceEntryType.ServiceFee,
	FinanceEntryType.ManagementFee,
	FinanceEntryType.BillByHousehold,
];

const entriesBottom = [
	FinanceEntryType.ContributionInfo,
	FinanceEntryType.QuarterlyReport,
];
</script>

<template>
	<div class="flex-col flex justify-between">
		<SidebarEntry title="quản lý thu phí" />
		<ul class="mx-1 flex flex-col items-start justify-center font-medium">
			<li v-for="entry in entriesTop" :key="entry" class="text-primary">
				<button class="max-w-[290px] whitespace-nowrap bg-transparent py-1 hover:border-transparent"
					:class="currentEntry === entry ? 'font-bold' : ''" @click="$emit('update:currentEntry', entry)">
					{{ entry }}
				</button>
			</li>
		</ul>
		<SidebarEntry title="quản lý đóng góp" />
		<ul class="mx-1 flex flex-col items-start justify-center font-medium">
			<li v-for="entry in entriesBottom" :key="entry" class="text-primary">
				<button class="bg-transparent py-1 pr-0 hover:border-transparent"
					:class="currentEntry === entry ? 'font-bold' : ''" @click="$emit('update:currentEntry', entry)">
					{{ entry }}
				</button>
			</li>
		</ul>
		<div class="flex-grow-[100]" />
		<button class="btn btn-primary w-40 self-center mt-4 mb-4" @click="make_payments">Tạo hoá đơn cho tháng</button>
		<div class="mb-4" v-if="output">{{ output }}</div>
	</div>
</template>
