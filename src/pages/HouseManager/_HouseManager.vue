<script setup lang="ts">
import NavigationBar from "../../components/NavigationBar.vue";
import RightSideContainer from "../../components/RightSideContainer.vue";
import Sidebar from "./SideBar.vue";
import HouseEntryType from "./entries";
import AddNewHousehold from "./EntryComponents/AddNewHousehold.vue";
import AddNewPerson from "./EntryComponents/AddNewPerson.vue";
import ChangeHouseholder from "./EntryComponents/ChangeHouseholder.vue";
import AddPersonToHousehold from "./EntryComponents/AddPersonToHousehold.vue";
import Deceased from "./EntryComponents/DedgePerson.vue";
import MoveOut from "./EntryComponents/MoveOut.vue";
import SplitHousehold from "./EntryComponents/SplitHousehold.vue";
import TemporaryResidence from "./EntryComponents/TemporaryResidence.vue";
import { ref } from "vue";
const currentEntryRef = ref(HouseEntryType.AddNewPerson);
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
				<AddNewHousehold
					v-if="currentEntryRef === HouseEntryType.AddNewHousehold"
				/>
				<AddPersonToHousehold
					v-if="
						currentEntryRef === HouseEntryType.AddPersonToHousehold
					"
				/>
				<AddNewPerson
					v-if="currentEntryRef === HouseEntryType.AddNewPerson"
				/>
				<ChangeHouseholder
					v-if="currentEntryRef === HouseEntryType.ChangeHouseholder"
				/>
				<Deceased
					v-if="currentEntryRef === HouseEntryType.DedgePerson"
				/>
				<MoveOut v-if="currentEntryRef === HouseEntryType.MoveOut" />
				<SplitHousehold
					v-if="currentEntryRef === HouseEntryType.SplitHousehold"
				/>
				<TemporaryResidence
					v-if="currentEntryRef === HouseEntryType.TemporaryResidence"
				/>
			</RightSideContainer>
		</div>
	</div>
</template>
