<script setup lang="ts">
import { PropType, ref } from "vue";
import { SpendingsTableViewType } from "./SpendingsTableViewType";

const props = defineProps({
	data: {
		type: Array as PropType<SpendingsTableViewType>,
		required: true,
	},
});

const dataSplitted = ref<SpendingsTableViewType[]>([]);
const dataPerPage = ref(10);
const currentPage = ref(1);
const totalPages = Math.ceil(props.data.length / dataPerPage.value);

function splitData() {
	dataSplitted.value = [];
	let temp: SpendingsTableViewType = [];
	for (let i = 0; i < props.data.length; i++) {
		if (i % dataPerPage.value === 0) {
			dataSplitted.value.push(temp);
			temp = [];
		}
		temp.push(props.data[i]);
	}
	dataSplitted.value.push(temp);
}

splitData();

function nextPage() {
	if (currentPage.value + 1 > totalPages) {
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
	currentPage.value = totalPages;
}

const currentlyModifying = ref(-1);
const new_id = ref("");
const new_date = ref("");
const new_household_id = ref("");
const new_total = ref("");
const new_description = ref("");

function deleteEntry(index: number) {
	props.data.splice(index, 1);
}

function modifyEntry(index: number) {
	if (index < 0 || index >= props.data.length) {
		return;
	}
	currentlyModifying.value = index;
}

function saveModification() {
	if (
		currentlyModifying.value < 0 ||
		currentlyModifying.value >= props.data.length
	) {
		return;
	}
	props.data[currentlyModifying.value].date = new_date.value;
	props.data[currentlyModifying.value].description = new_description.value;
	props.data[currentlyModifying.value].household_id = new_household_id.value;
	props.data[currentlyModifying.value].total = new_total.value;
	currentlyModifying.value = -1;
	new_id.value = "";
	new_description.value = "";
	new_date.value = "";
	new_household_id.value = "";
	new_total.value = "";
}

function cancelModification() {
	currentlyModifying.value = -1;
	new_id.value = "";
	new_description.value = "";
	new_date.value = "";
	new_household_id.value = "";
	new_total.value = "";
}
</script>
<template>
	<div
		class="h-120 flex flex-col items-center justify-center gap-4 overflow-y-auto"
	>
		<table v-if="props.data.length">
			<thead class="[&_th]:min-w-[200px] [&_th]:px-4 [&_th]:py-2">
				<tr>
					<th>Mã</th>
					<th>Nhà đóng góp</th>
					<th>Ngày đóng góp</th>
					<th>Nội dung</th>
					<th>Tổng giá trị</th>
					<th>Hành động</th>
				</tr>
			</thead>
			<tbody
				class="[&_td]:min-w-[200px] [&_td]:border [&_td]:px-4 [&_td]:py-2"
			>
				<tr v-for="(item, index) in dataSplitted[currentPage]">
					<td>{{ item.id }}</td>
					<td>{{ item.household_id }}</td>
					<td>{{ item.date }}</td>
					<td>{{ item.description }}</td>
					<td>{{ item.total }}</td>
					<td class="flex items-center justify-center gap-2">
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
						</button>
					</td>
				</tr>
			</tbody>
		</table>
		<div v-else class="text-center">
			<h1 class="text-2xl font-bold">Không có dữ liệu</h1>
		</div>
		<div
			v-show="currentlyModifying !== -1"
			class="flex flex-row items-center justify-center gap-4"
		>
			<input
				v-model="new_date"
				type="text"
				placeholder="Ngày đóng góp"
				class="input input-bordered w-full"
			/>
			<input
				v-model="new_household_id"
				type="text"
				placeholder="Nhà đóng góp"
				class="input input-bordered w-full"
			/>
			<input
				v-model="new_description"
				type="text"
				placeholder="Nội dung"
				class="input input-bordered w-full"
			/>
			<input
				v-model="new_total"
				type="text"
				placeholder="Tổng giá trị"
				class="input input-bordered w-full"
			/>
			<button class="btn btn-primary btn-sm" @click="saveModification()">
				Lưu
			</button>
			<button class="btn btn-error btn-sm" @click="cancelModification()">
				Hủy
			</button>
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
	</div>
</template>
