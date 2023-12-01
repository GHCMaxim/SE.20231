<script setup lang="ts">
import SidebarEntry from "../../components/SidebarEntry.vue";
import HouseEntryType from "./entries";

defineProps({
	currentEntry: {
		type: String,
		required: true,
	},
});

defineEmits(["update:currentEntry"]);

const entriesTop = [
	HouseEntryType.AddNewPerson,
	HouseEntryType.AddNewHousehold,
	HouseEntryType.SplitHousehold,
	HouseEntryType.ChangeHouseholder,
];

const entriesBottom = [
	HouseEntryType.TemporaryResidence,
	HouseEntryType.MoveOut,
	HouseEntryType.DedgePerson,
];
</script>

<template>
	<div>
		<SidebarEntry title="quản lý thu phí" />
		<ul
			class="mx-1 flex flex-col items-start justify-center font-medium [&_button]:bg-transparent [&_button]:py-1 [&_button]:outline-none [&_button]:hover:border-transparent [&_li]:text-primary"
		>
			<li v-for="entry in entriesTop" :key="entry">
				<button
					:class="currentEntry === entry ? 'font-bold' : ''"
					@click="$emit('update:currentEntry', entry)"
				>
					{{ entry }}
				</button>
			</li>
		</ul>
		<SidebarEntry title="quản lý đóng góp" />
		<ul
			class="mx-1 flex flex-col items-start justify-center font-medium [&_button]:bg-transparent [&_button]:py-1 [&_button]:outline-none [&_button]:hover:border-transparent [&_li]:text-primary"
		>
			<li v-for="entry in entriesBottom" :key="entry">
				<button
					:class="currentEntry === entry ? 'font-bold' : ''"
					@click="$emit('update:currentEntry', entry)"
				>
					{{ entry }}
				</button>
			</li>
		</ul>
	</div>
</template>
