<script setup lang="ts">
import NavigationBar from "../../components/NavigationBar.vue";
import RightSideContainer from "../../components/RightSideContainer.vue";
import Sidebar from "./SideBar.vue";
import RewardEntryType from "./entries";
import RewardCreate from "./EntryComponent/RewardCreate.vue";
import RewardList from "./EntryComponent/RewardList.vue";
import { ref } from "vue";

const currentEntryRef = ref(RewardEntryType.RewardList);
</script>

<template>
	<div>
		<NavigationBar />
		<div class="flex flex-row">
			<Sidebar
				:current-entry="currentEntryRef"
				@update:current-entry="currentEntryRef = $event"
			/>
			<RightSideContainer>
				<Suspense>
					<RewardList
						v-if="currentEntryRef === RewardEntryType.RewardList"
					/>
				</Suspense>
				<RewardCreate
					v-if="currentEntryRef === RewardEntryType.RewardCreate"
				/>
			</RightSideContainer>
		</div>
	</div>
</template>
