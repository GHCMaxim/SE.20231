<script setup lang="ts">
import { PropType, ref, computed, watchEffect } from "vue";
import { PaymentByHouseholdType } from "./PaymentByHouseholdType";

const props = defineProps({
	data: {
		type: Array as PropType<PaymentByHouseholdType>,
		required: true,
	},
});
const currentlyModifying = ref(-1);
const current_typeID = ref("");
const current_id = ref("");
const current_incomeID = ref("");
const current_creationDate = ref("");

const dataSplitted = ref<PaymentByHouseholdType[]>([]);
const dataPerPage = ref(10);
const currentPage = ref(1);
const searchTerm = ref("");
const filteredData = computed(() => {
	if (!searchTerm.value) {
		return props.data;
	}
	return props.data.filter((item) =>
		item.household.toLowerCase().includes(searchTerm.value.toLowerCase()),
	);
});

const totalPages = computed(() =>
	Math.ceil(filteredData.value.length / dataPerPage.value),
);
function splitData() {
	dataSplitted.value = [];
	let temp: PaymentByHouseholdType = [];
	for (let i = 0; i < filteredData.value.length; i++) {
		if (i % dataPerPage.value === 0) {
			dataSplitted.value.push(temp);
			temp = [];
		}
		temp.push(filteredData.value[i]);
	}
	dataSplitted.value.push(temp);
}

function seeDetails(index: number){
	if(index < 0 || index >= props.data.length){
		return;
	}
	currentlyModifying.value = index;
	current_typeID.value =(props.data[index].type_id).toString();
	current_id.value = (props.data[index].id).toString();
	current_incomeID.value = (props.data[index].income_id).toString();
	current_creationDate.value = props.data[index].creation_date;
}

function Ok(){
	currentlyModifying.value = -1;
	current_typeID.value = "";
	current_id.value = "";
	current_incomeID.value = "";
	current_creationDate.value = "";
}
splitData();

function nextPage() {
	const totalPagesValue = totalPages.value;
	if (currentPage.value + 1 > totalPagesValue) {
		return;
	}
	currentPage.value++;
}

function prevPage() {
	if (currentPage.value - 1 < 1) {
		return;
	}
	currentPage.value--;
}

function firstPage() {
	currentPage.value = 1;
}

function lastPage() {
	currentPage.value = totalPages.value;
}

// function deleteEntry(index: number) {
// 	props.data.splice(index, 1);
// }

// function modifyEntry(index: number) {
// 	if (index < 0 || index >= props.data.length) {
// 		return;
// 	}
// 	currentlyModifying.value = index;
// }

// function saveModification() {
// 	if (
// 		currentlyModifying.value < 0 ||
// 		currentlyModifying.value >= props.data.length
// 	) {
// 		return;
// 	}
// 	props.data[currentlyModifying.value].date = new_date.value;
// 	props.data[currentlyModifying.value].description = new_description.value;
// 	props.data[currentlyModifying.value].household_id = new_household_id.value;
// 	props.data[currentlyModifying.value].total = new_total.value;
// 	currentlyModifying.value = -1;
// 	new_id.value = "";
// 	new_description.value = "";
// 	new_date.value = "";
// 	new_household_id.value = "";
// 	new_total.value = "";
// }

// function cancelModification() {
// 	currentlyModifying.value = -1;
// 	new_id.value = "";
// 	new_description.value = "";
// 	new_date.value = "";
// 	new_household_id.value = "";
// 	new_total.value = "";
// }
watchEffect(() => {
	splitData();
});
</script>
<template>
	<div
		class="h-120 flex flex-col items-center justify-center gap-4 overflow-y-auto"
	>
		<div class="search-container">
			<input
				v-model="searchTerm"
				class="mx-auto my-2 rounded border bg-white"
				type="text"
				placeholder=" Tìm kiếm mã hộ khẩu..."
			/>
		</div>
		<table v-if="props.data.length">
			<thead class="[&_th]:min-w-[200px] [&_th]:px-4 [&_th]:py-2">
				<tr>
					<th>Hộ khẩu</th>
					<th>Tên hoá đơn</th>
					<th>Giá trị</th>
					<th>Đã trả</th>
					<th>Hành động</th>
				</tr>
			</thead>
			<tbody
				class="[&_td]:min-w-[200px] [&_td]:border [&_td]:px-4 [&_td]:py-2"
			>
				<tr v-for="(item,index) in dataSplitted[currentPage]" :key="index">
					<td>{{ item.household }}</td>
					<td>{{ item.name }}</td>
					<td>{{ item.price }}</td>
					<td>{{ item.paid }}</td>
					<td>
						<button
							class="btn btn-primary btn-sm"
							@click="seeDetails(index)"
						>
							Xem chi tiết
						</button>
					</td>
					<!-- <td class="flex items-center justify-center gap-2">
						<button
							class="btn btn-primary btn-sm"
							@click="modifyEntry(index)"
						>
							Chỉnh sửa
						</button>
						<button
							class="btn btn-error btn-sm"
							@click="deleteEntry(index)"
						>
							Xóa
						</button> -->
					<!-- </td> -->
				</tr>
			</tbody>
		</table>
		<div v-else class="text-center">
			<h1 class="text-2xl font-bold">Không có dữ liệu</h1>
		</div>
		<div v-show="currentlyModifying !== -1" class="popup">
			<div class="popup-content">
				<h2>Thông tin chi tiết</h2>
				<p>Mã hoá đơn {{ current_id }} </p>
				<p>Loại hoá đơn {{ current_typeID }} </p>
				<p>Mã thu nhập {{ current_incomeID }} </p>
				<p>Ngày tạo {{ current_creationDate }} </p>
				<button class="btn btn-primary btn-sm" @click="Ok()">OK</button>
			</div>
		</div>
	</div>
	<div class="flex flex-row items-center justify-center gap-4">
		<button
			class="btn btn-primary btn-sm"
			:disabled="currentPage === 1"
			@click="firstPage()"
		>
			Trang đầu
		</button>
		<button
			class="btn btn-primary btn-sm"
			:disabled="currentPage === 1"
			@click="prevPage()"
		>
			Trang trước
		</button>
		<button
			class="btn btn-primary btn-sm"
			:disabled="currentPage === totalPages"
			@click="nextPage()"
		>
			Trang sau
		</button>
		<button
			class="btn btn-primary btn-sm"
			:disabled="currentPage === totalPages"
			@click="lastPage()"
		>
			Trang cuối
		</button>
	</div>
</template>

<style scoped>
.popup {
	position: fixed;
	top: 0;
	left: 0;
	width: 100%;
	height: 100%;
	background-color: rgba(0, 0, 0, 0.5);
	display: flex;
	justify-content: center;
	align-items: center;
}

.popup-content {
	background-color: white;
	padding: 20px;
	border-radius: 10px;
}
</style>