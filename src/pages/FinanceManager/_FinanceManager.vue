<script setup lang="ts">
import NavigationBar from "../../components/NavigationBar.vue";
import RightSideContainer from "../../components/RightSideContainer.vue";
import SideBar from "./SideBar.vue";
import BillEssentials from "./EntryComponents/BillEssentials.vue";
import BillByHousehold from "./EntryComponents/BillByHousehold.vue";
import ContributionInfo from "./EntryComponents/ContributionInfo.vue";
import ParkingFee from "./EntryComponents/ParkingFee.vue";
import ServiceFee from "./EntryComponents/ServiceFee.vue";
import CreateContributionEvent from "./EntryComponents/CreateContributionEvent.vue";
import CreateContribution from "./EntryComponents/CreateContribution.vue";
import FinanceEntryType from "./entries";
import { ref } from "vue";

const currentEntryRef = ref(FinanceEntryType.ParkingFee);
</script>

<template>
	<div>
		<NavigationBar />
		<div class="flex flex-row">
			<SideBar :current-entry="currentEntryRef" @update:current-entry="currentEntryRef = $event" />
			<RightSideContainer>
				<Suspense>
					<ParkingFee v-if="currentEntryRef === FinanceEntryType.ParkingFee" />
				</Suspense>
				<Suspense>
					<BillEssentials v-if="currentEntryRef === FinanceEntryType.BillEssentials
						" />
				</Suspense>
				<Suspense>
					<ServiceFee v-if="currentEntryRef === FinanceEntryType.ServiceFee" />
				</Suspense>
				<Suspense>
					<BillByHousehold v-if="currentEntryRef === FinanceEntryType.BillByHousehold
						" />
				</Suspense>

				<Suspense>
					<CreateContributionEvent v-if="currentEntryRef ===
						FinanceEntryType.CreateContributionEvent
						" />
				</Suspense>
				<Suspense>
					<CreateContribution v-if="currentEntryRef === FinanceEntryType.CreateContribution
						" />
				</Suspense>
				<Suspense>
					<ContributionInfo v-if="currentEntryRef ===
						FinanceEntryType.ContributionInfo
						" />
				</Suspense>

			</RightSideContainer>
		</div>
	</div>
</template>
