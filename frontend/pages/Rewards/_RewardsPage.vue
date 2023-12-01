<script setup lang="ts">
import NavigationBar from "../../components/NavigationBar.vue";
import SidebarEntry from "../../components/SidebarEntry.vue";
import RightSideContainer from "../../components/RightSideContainer.vue";
import RewardEntryType from "./entries";
import { ref } from "vue";

const entries = [
	RewardEntryType.RewardList,
	RewardEntryType.RewardHistory,
	RewardEntryType.RewardCreate,
];

const currentEntryRef = ref(RewardEntryType.RewardList);
</script>

<template>
	<div>
		<NavigationBar />
		<div class="flex flex-row">
			<div class="flex flex-col">
				<SidebarEntry title="Quản lý khen thưởng" />
				<ul
					class="mx-1 flex flex-col items-start justify-center font-medium [&_button]:bg-transparent [&_button]:py-1 [&_button]:outline-none [&_button]:hover:border-transparent [&_li]:text-primary"
				>
					<li v-for="entry in entries" :key="entry">
						<button
							:class="
								currentEntryRef === entry ? 'font-bold' : ''
							"
							@click="currentEntryRef = entry"
						>
							{{ entry }}
						</button>
					</li>
				</ul>
			</div>
			<RightSideContainer>Placeholder</RightSideContainer>
		</div>
	</div>
</template>
