<script setup lang="ts">
import { PropType, ref, computed, watchEffect } from "vue";
import { RewardTableViewType } from "./RewardTableViewType";

const props = defineProps({
	data: {
		type: Array as PropType<RewardTableViewType>,
		required: true,
	},
});

const dataSplitted = ref<RewardTableViewType[]>([]);
const dataPerPage = ref(10);
const currentPage = ref(1);
const totalPages = Math.ceil(props.data.length / dataPerPage.value);

const searchTerm = ref("");
const filteredData = computed(() => {
	if (!searchTerm.value) {
		return props.data;
	}
	return props.data.filter((item) =>
		item.id.toString().includes(searchTerm.value.toLowerCase()),
	);
});

function splitData() {
	dataSplitted.value = [];
	let temp: RewardTableViewType = [];
	for (let i = 0; i < props.data.length; i++) {
		if (i % dataPerPage.value === 0) {
			dataSplitted.value.push(temp);
			temp = [];
		}
		temp.push(filteredData.value[i]);
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
const newdate = ref("");
const newrecipient = ref("");
const newreward_type_id = ref("");

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
	props.data[currentlyModifying.value].date = newdate.value;
	props.data[currentlyModifying.value].recipient = newrecipient.value;
	props.data[currentlyModifying.value].reward_type_id =
		newreward_type_id.value;
	currentlyModifying.value = -1;
	new_id.value = "";
	newdate.value = "";
	newrecipient.value = "";
	newreward_type_id.value = "";
}

function cancelModification() {
	currentlyModifying.value = -1;
	new_id.value = "";
	newdate.value = "";
	newrecipient.value = "";
	newreward_type_id.value = "";
}

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
				placeholder=" Tìm kiếm theo mã PT..."
			/>
		</div>
		<table v-if="props.data.length">
			<thead class="[&_th]:min-w-[200px] [&_th]:px-4 [&_th]:py-2">
				<tr>
					<th>Mã</th>
					<th>Ngày nhận</th>
					<th>Người nhận</th>
					<th>Loại quà</th>
					<th>Hành động</th>
				</tr>
			</thead>
			<tbody
				class="[&_td]:min-w-[200px] [&_td]:border [&_td]:px-4 [&_td]:py-2"
			>
				<tr v-for="(item, index) in dataSplitted[currentPage]">
					<td>{{ item.id }}</td>
					<td>{{ item.date }}</td>
					<td>{{ item.recipient }}</td>
					<td>{{ item.reward_type_id }}</td>
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
				v-model="newdate"
				type="date"
				placeholder="new date"
				class="input input-bordered w-full"
			/>
			<input
				v-model="newrecipient"
				type="text"
				placeholder="new recipient"
				class="input input-bordered w-full"
			/>
			<input
				v-model="newreward_type_id"
				type="text"
				placeholder="new reward_type_id"
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
