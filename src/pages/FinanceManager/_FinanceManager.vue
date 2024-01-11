<script setup lang="ts">
import NavigationBar from "../../components/NavigationBar.vue";
import RightSideContainer from "../../components/RightSideContainer.vue";
import SideBar from "./SideBar.vue";
import BillEssentials from "./EntryComponents/BillEssentials.vue";
import BillByHousehold from "./EntryComponents/BillByHousehold.vue";
import ContributionInfo from "./EntryComponents/ContributionInfo.vue";
import ManagementFee from "./EntryComponents/ManagementFee.vue";
import ParkingFee from "./EntryComponents/ParkingFee.vue";
import QuarterlyReport from "./EntryComponents/QuarterlyReport.vue";
import ServiceFee from "./EntryComponents/ServiceFee.vue";
import FinanceEntryType from "./entries";
import { ref } from "vue";

const currentEntryRef = ref(FinanceEntryType.ParkingFee);
</script>

<template>
	<div>
		<NavigationBar />
		<div class="flex flex-row">
			<SideBar
				:current-entry="currentEntryRef"
				@update:current-entry="currentEntryRef = $event"
			/>
			<RightSideContainer>
				<Suspense>
					<BillEssentials
						v-if="
							currentEntryRef === FinanceEntryType.BillEssentials
						"
					/>
				</Suspense>
				<Suspense>
					<BillByHousehold
						v-if="
							currentEntryRef === FinanceEntryType.BillByHousehold
						"
					/>
				</Suspense>
				<Suspense>
					<ContributionInfo
						v-if="
							currentEntryRef ===
							FinanceEntryType.ContributionInfo
						"
					/>
				</Suspense>
				<Suspense>
					<ManagementFee
						v-if="
							currentEntryRef === FinanceEntryType.ManagementFee
						"
					/>
				</Suspense>
				<Suspense>
					<ParkingFee
						v-if="currentEntryRef === FinanceEntryType.ParkingFee"
					/>
				</Suspense>
				<QuarterlyReport
					v-if="currentEntryRef === FinanceEntryType.QuarterlyReport"
				/>
				<Suspense>
					<ServiceFee
						v-if="currentEntryRef === FinanceEntryType.ServiceFee"
					/>
				</Suspense>
			</RightSideContainer>
		</div>
	</div>
</template>
