<script setup lang="ts">
import { PropType, ref } from "vue";
import { ContributionsTableViewType } from "./ContributionsTableViewType";
import { API } from "../store";
const props = defineProps({
	data: {
		type: Array as PropType<ContributionsTableViewType>,
		required: true,
	},
});

const dataSplitted = ref<ContributionsTableViewType[]>([]);
const dataPerPage = ref(10);
const currentPage = ref(1);
const totalPages = Math.ceil(props.data.length / dataPerPage.value);

const currentlyModifying = ref(-1);
const new_id = ref("");
const new_contributor = ref("");
const new_amount = ref("");
const new_description = ref("");
const new_contribution_date = ref("");
const new_contribution_event = ref("");
function splitData() {
	dataSplitted.value = [];
	let temp: ContributionsTableViewType = [];
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

function deleteEntry(index: number) {
	props.data.splice(index, 1);
}

function modifyEntry(index: number) {
	if (index < 0 || index >= props.data.length) {
		return;
	}
	currentlyModifying.value = index;
}

async function saveModification() {
	if (
		currentlyModifying.value < 0 ||
		currentlyModifying.value >= props.data.length
	) {
		return;
	}
	props.data[currentlyModifying.value].contributor = new_contributor.value;
	props.data[currentlyModifying.value].amount = parseInt(new_amount.value);
	props.data[currentlyModifying.value].description = new_description.value;
	props.data[currentlyModifying.value].contribution_date =
		new_contribution_date.value;
	props.data[currentlyModifying.value].contribution_event = parseInt(new_contribution_event.value);
	currentlyModifying.value = -1;
	new_contributor.value = "";
	new_amount.value = "";
	new_description.value = "";
	new_contribution_date.value = "";
	new_contribution_event.value = "";
	new_id.value = "";
	try {
		const response = await fetch(
			API + "/contributions/" + props.data[currentlyModifying.value].id,
			{
				method: "PUT",
				headers: {
					"Content-Type": "application/json",
					accept: "application/json",
				},
				body: JSON.stringify({
					id: props.data[currentlyModifying.value].id,
					contributor: new_contributor.value,
					amount: parseInt(new_amount.value),
					description: new_description.value,
					contribution_date: new_contribution_date.value,
					contribution_event: new_contribution_event.value,
				}),
			},
		);
		if (!response.ok) {
			console.error(response.statusText);
		}
	} catch (error) {
		console.error(error);
	}
}

function cancelModification() {
	currentlyModifying.value = -1;
	new_id.value = "";
	new_description.value = "";
	new_amount.value = "";
	new_contributor.value = "";
	new_contribution_date.value = "";
}
</script>
<template>
	<div class="h-120 flex flex-col items-center justify-center gap-4 overflow-y-auto">
		<table v-if="props.data.length">
			<thead class="[&_th]:min-w-[200px] [&_th]:px-4 [&_th]:py-2">
				<tr>
					<th>ID</th>
					<th>CCCD người đóng góp</th>
					<th>Khoản đóng góp</th>
					<th>Nội dung</th>
					<th>Ngày đóng góp</th>
					<th>Mã hđ đóng góp</th>
					<th>Thao tác</th>
				</tr>
			</thead>
			<tbody class="[&_td]:min-w-[200px] [&_td]:border [&_td]:px-4 [&_td]:py-2">
				<tr v-for="(item, index) in dataSplitted[currentPage]">
					<td>{{ item.id }}</td>
					<td>{{ item.contributor }}</td>
					<td>{{ item.amount }}</td>
					<td>{{ item.description }}</td>
					<td>{{ item.contribution_date }}</td>
					<td>{{ item.contribution_event }}</td>
					<td class="flex items-center justify-center gap-2">
						<button class="btn btn-primary btn-sm" @click="modifyEntry(index)">
							Chỉnh sửa
						</button>
						<button class="btn btn-error btn-sm" @click="deleteEntry(index)">
							Xóa
						</button>
					</td>
				</tr>
			</tbody>
		</table>
		<div v-else class="text-center">
			<h1 class="text-2xl font-bold">Không có dữ liệu</h1>
		</div>
		<div v-show="currentlyModifying !== -1" class="flex flex-row items-center justify-center gap-4">
			<input v-model="new_contributor" type="number" placeholder="CCCD người đóng góp"
				class="input input-bordered w-full" />
			<input v-model="new_amount" type="number" placeholder="Khoản đóng góp" class="input input-bordered w-full" />
			<input v-model="new_description" type="text" placeholder="Nội dung" class="input input-bordered w-full" />
			<input v-model="new_contribution_date" type="date" placeholder="Ngày đóng góp"
				class="input input-bordered w-full" />
			<input v-model="new_contribution_event" type="number" placeholder="Mã hđ đóng góp"
				class="input input-bordered w-full" />
			<button class="btn btn-primary btn-sm" @click="saveModification()">
				Lưu
			</button>
			<button class="btn btn-error btn-sm" @click="cancelModification()">
				Hủy
			</button>
		</div>
	</div>
	<div class="flex flex-row items-center justify-center gap-4">
		<button class="btn btn-primary btn-sm" :disabled="currentPage === 1" @click="firstPage()">
			Trang đầu
		</button>
		<button class="btn btn-primary btn-sm" :disabled="currentPage === 1" @click="prevPage()">
			Trang trước
		</button>
		<button class="btn btn-primary btn-sm" :disabled="currentPage === totalPages" @click="nextPage()">
			Trang sau
		</button>
		<button class="btn btn-primary btn-sm" :disabled="currentPage === totalPages" @click="lastPage()">
			Trang cuối
		</button>
	</div>
</template>
