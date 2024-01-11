<script setup lang="ts">
import { ref, watch } from "vue";
import NavigationBar from "../components/NavigationBar.vue";
import SidebarEntry from "../components/SidebarEntry.vue";
import RightSideContainer from "../components/RightSideContainer.vue";
import HouseholdTableView from "../components/HouseholdTableView.vue";
import PeopleTableView from "../components/PeopleTableView.vue";
import RewardTableTypeView from "../components/RewardTableTypeView.vue";
import PaymentByHouseholdView from "../components/PaymentByHouseholdView.vue";
import { API } from "../store";
import { HouseholdTableViewType } from "../components/HouseholdTableViewType";
import { PeopleTableViewType } from "../components/PeopleTableViewType";
import { RewardTableType } from "../components/RewardTableType";
import { PaymentByHouseholdType } from "../components/PaymentByHouseholdType";
const HouseholdData = ref<HouseholdTableViewType>([]);
const PeopleData = ref<PeopleTableViewType>([]);
const RewardData = ref<RewardTableType>([]);
const PaymentData = ref<PaymentByHouseholdType>([]);

const inputValue = ref("");

async function getData(){
	let endpoint;
	switch(currentSearchCategory.value){
		case SearchCategory.HouseholdInfo:
			endpoint = `/api/households/${inputValue.value}`;
			break;
		case SearchCategory.PersonInfo:
			endpoint = `/api/people/${inputValue.value}`;
			break;
		case SearchCategory.Contributions:
			endpoint = `/api/payments/by_household/${inputValue.value}`;
			break;
		case SearchCategory.Rewards:
			endpoint = `/api/rewards/${inputValue.value}`;
			break;
	}
	const response = await fetch(API + endpoint);
	const data = await response.json();
	switch(currentSearchCategory.value){
		case SearchCategory.HouseholdInfo:
			HouseholdData.value = data;
			break;
		case SearchCategory.PersonInfo:
			PeopleData.value = data;
			break;
		case SearchCategory.Contributions:
			PaymentData.value = data;
			break;
		case SearchCategory.Rewards:
			RewardData.value = data;
			break;
	}
}

enum SearchCategory {
	HouseholdInfo = "Thông tin về hộ khẩu",
	PersonInfo = "Thông tin về nhân khẩu",
	Contributions = "Phí thu theo hộ",
	Rewards = "Danh sách phần thưởng",
}

const correspondFields = [
	["Số hộ khẩu", "Nhập số hộ khẩu", SearchCategory.HouseholdInfo],
	["Số căn cước", "Nhập số căn cước", SearchCategory.PersonInfo],
	["Số hộ khẩu", "Nhập số hộ khẩu", SearchCategory.Contributions],
	["Mã đợt khen thưởng", "Nhập mã đợt khen thưởng", SearchCategory.Rewards],
];

const searchCategoryTitle = ref(correspondFields[0][0]);
const searchCategoryPlaceholder = ref(correspondFields[0][1]);
const currentSearchCategory = ref(SearchCategory.HouseholdInfo);

function changeSearchCategory(index: number) {
	searchCategoryTitle.value = correspondFields[index][0];
	searchCategoryPlaceholder.value = correspondFields[index][1];
	currentSearchCategory.value = correspondFields[index][2] as SearchCategory;
}

watch(currentSearchCategory, async (newVal, oldVal) => {
    if (newVal !== oldVal) {
        await getData();
    }
});


</script>

<template>
	<div class="h-screen">
		<NavigationBar />
		<div class="flex h-[calc(100vh-160px)] flex-row">
			<div class="flex flex-col">
				<SidebarEntry title="tìm kiếm" icon="search" />
				<div class="px-10">
					<div class="mb-3 text-start">Tìm kiếm theo</div>
					<select
						class="select select-primary w-full max-w-xs"
						title="Chọn"
						@change="
							// @ts-ignore
							changeSearchCategory($event.target?.selectedIndex)
						"
					>
						<option
							v-for="(field, index) in correspondFields"
							:key="index"
							:selected="index === 0"
						>
							{{ field[2] }}
						</option>
					</select>
					<div class="my-3 text-start">
						{{ searchCategoryTitle }}
					</div>
					<input
						type="text"
						:placeholder="searchCategoryPlaceholder"
						class="input input-bordered w-full max-w-xs"
					/>
					<button class="btn btn-primary w-full mt-4" @click="getData()">Tìm kiếm</button>
				</div>
			</div>

			<RightSideContainer> 
				<div v-if="currentSearchCategory === SearchCategory.HouseholdInfo" >
					<HouseholdTableView :data="HouseholdData" />
				</div>
				<div v-else-if="currentSearchCategory === SearchCategory.PersonInfo" >
					<PeopleTableView :data="PeopleData" />
				</div>
				<div v-else-if="currentSearchCategory === SearchCategory.Contributions" >
					<PaymentByHouseholdView :data="PaymentData" />
				</div>
				<div v-else-if="currentSearchCategory === SearchCategory.Rewards" >
					<RewardTableTypeView :data="RewardData" />
				</div>
			</RightSideContainer>
		</div>
	</div>
</template>
