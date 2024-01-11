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
	HouseEntryType.AddPersonToHousehold,
	HouseEntryType.SplitHousehold,
	HouseEntryType.ChangeHouseholder,
	HouseEntryType.AddVehicleToHousehold,
];

const entriesBottom = [
	HouseEntryType.TemporaryResidence,
	HouseEntryType.MoveOut,
	HouseEntryType.DedgePerson,
];
</script>

<template>
	<div>
		<SidebarEntry title="quản lý hộ khẩu" />
		<ul class="mx-1 flex flex-col items-start justify-center font-medium">
			<li v-for="entry in entriesTop" :key="entry" class="text-primary">
				<button :class="currentEntry === entry ? 'font-bold' : ''"
					class="bg-transparent py-1 hover:border-transparent" @click="$emit('update:currentEntry', entry)">
					{{ entry }}
				</button>
			</li>
		</ul>
		<SidebarEntry title="quản lý nhân khẩu" />
		<ul class="mx-1 flex flex-col items-start justify-center font-medium">
			<li v-for="entry in entriesBottom" :key="entry" class="text-primary">
				<button :class="currentEntry === entry ? 'font-bold' : ''"
					class="bg-transparent py-1 outline-none hover:border-transparent"
					@click="$emit('update:currentEntry', entry)">
					{{ entry }}
				</button>
			</li>
		</ul>
		<button class="btn btn-primary w-80 self-center">Thing</button>

	</div>
</template>
