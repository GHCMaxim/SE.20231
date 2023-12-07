<script setup lang="ts">
import SidebarEntry from "../../components/SidebarEntry.vue";
import FinanceEntryType from "./entries";

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
	FinanceEntryType.UpdateContribution,
	FinanceEntryType.QuarterlyReport,
];
</script>

<template>
	<div>
		<SidebarEntry title="quản lý thu phí" />
		<ul class="mx-1 flex flex-col items-start justify-center font-medium">
			<li v-for="entry in entriesTop" :key="entry" class="text-primary">
				<button
					class="max-w-[290px] whitespace-nowrap bg-transparent py-1 hover:border-transparent"
					:class="currentEntry === entry ? 'font-bold' : ''"
					@click="$emit('update:currentEntry', entry)"
				>
					{{ entry }}
				</button>
			</li>
		</ul>
		<SidebarEntry title="quản lý đóng góp" />
		<ul class="mx-1 flex flex-col items-start justify-center font-medium">
			<li
				v-for="entry in entriesBottom"
				:key="entry"
				class="text-primary"
			>
				<button
					class="bg-transparent py-1 pr-0 hover:border-transparent"
					:class="currentEntry === entry ? 'font-bold' : ''"
					@click="$emit('update:currentEntry', entry)"
				>
					{{ entry }}
				</button>
			</li>
		</ul>
	</div>
</template>
