<script setup lang="ts">
import { ref } from "vue";
import NavigationBar from "../components/NavigationBar.vue";
import SidebarEntry from "../components/SidebarEntry.vue";
import RightSideContainer from "../components/RightSideContainer.vue";

enum SearchCategory {
	HouseholdInfo = "Thông tin về hộ khẩu",
	PersonInfo = "Thông tin về nhân khẩu",
	Contributions = "Phí thu theo hộ",
	Contributors = "Các khoản đóng góp",
	Rewards = "Danh sách phần thưởng",
}

const correspondFields = [
	["Số hộ khẩu", "Nhập số hộ khẩu", SearchCategory.HouseholdInfo],
	["Số căn cước", "Nhập số căn cước", SearchCategory.PersonInfo],
	["Số hộ khẩu", "Nhập số hộ khẩu", SearchCategory.Contributions],
	[
		"Mã tài khoản đóng góp",
		"Nhập số tài khoản đóng góp",
		SearchCategory.Contributors,
	],
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
				</div>
			</div>

			<RightSideContainer> Search placeholder </RightSideContainer>
		</div>
	</div>
</template>
