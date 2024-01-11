<script setup lang="ts">
import SidebarEntry from "../../components/SidebarEntry.vue";
import FinanceEntryType from "./entries";
import { ref } from "vue";

const output = ref("");
async function make_payments() {
	const res = await fetch(
		"http://localhost:8000/api/payments/monthly/create",
	);
	if (!res.ok) {
		output.value = res.statusText;
		return;
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

const emit = defineEmits(["update:currentEntry"]);

const entriesTop = [
	FinanceEntryType.ParkingFee,
	FinanceEntryType.BillEssentials,
	FinanceEntryType.ServiceFee,
	FinanceEntryType.ManagementFee,
	FinanceEntryType.BillByHousehold,
];

const entriesBottom = [
	FinanceEntryType.CreateContributionEvent,
	FinanceEntryType.CreateContribution,
	FinanceEntryType.ContributionInfo,
	FinanceEntryType.QuarterlyReport,
];

async function handleEmit(entry: FinanceEntryType) {
	const token = document.cookie
		.split(";")
		.find((row) => row.startsWith("token"))
		?.split("=")[1];
	if (!token) {
		alert("Không tìm thấy token");
		return;
	}
	// base64 decode the second part of the token
	const payload = JSON.parse(atob(token.split(".")[1]));
	console.log(payload);

	emit("update:currentEntry", entry);
}
</script>

<template>
	<div class="flex flex-col justify-between">
		<SidebarEntry title="quản lý thu phí" />
		<ul class="mx-1 flex flex-col items-start justify-center font-medium">
			<li v-for="entry in entriesTop" :key="entry" class="text-primary">
				<button class="max-w-[290px] whitespace-nowrap bg-transparent py-1 hover:border-transparent"
					:class="currentEntry === entry ? 'font-bold' : ''" @click="handleEmit(entry)">
					{{ entry }}
				</button>
			</li>
		</ul>
		<SidebarEntry title="quản lý đóng góp" />
		<ul class="mx-1 flex flex-col items-start justify-center font-medium">
			<li v-for="entry in entriesBottom" :key="entry" class="text-primary">
				<button class="bg-transparent py-1 pr-0 hover:border-transparent"
					:class="currentEntry === entry ? 'font-bold' : ''" @click="handleEmit(entry)">
					{{ entry }}
				</button>
			</li>
		</ul>
		<div class="grow-[100]" />
		<button class="btn btn-primary my-4 w-40 self-center" @click="make_payments">
			Tạo hoá đơn cho tháng
		</button>
		<div v-if="output" class="mb-4">{{ output }}</div>
	</div>
</template>
