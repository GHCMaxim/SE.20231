<script setup lang="ts">
import SidebarEntry from "../../components/SidebarEntry.vue";
import RewardEntryType from "./entries";

defineProps({
	currentEntry: {
		type: String,
		required: true,
	},
});

defineEmits(["update:currentEntry"]);

const entriesTop = [RewardEntryType.RewardList, RewardEntryType.RewardCreate];
</script>

<template>
	<div>
		<SidebarEntry title="quản lý khen thưởng" />
		<ul class="flex flex-col items-start justify-center font-medium">
			<li v-for="entry in entriesTop" :key="entry" class="text-primary">
				<button
					:class="currentEntry === entry ? 'font-bold' : ''"
					class="bg-transparent py-1 hover:border-transparent"
					@click="$emit('update:currentEntry', entry)"
				>
					{{ entry }}
				</button>
			</li>
		</ul>
	</div>
</template>
