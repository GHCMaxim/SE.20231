<script setup lang="ts">
import RateTableView from "../../../components/RateTableView.vue";
import { ref } from "vue";
import { RateTableViewType } from "../../../components/RateTableViewType";
import SmallFormWrapper from "../../../components/SmallFormWrapper.vue";
import InputBox from "../../../components/InputBox.vue";

const res_data = ref<RateTableViewType>([]);

const id = ref("");

async function get_data() {
	const res = await fetch(
		`http://localhost:8000/api/payments/by_household/${id.value}`,
	);
	const data = await res.json();
	res_data.value = data;
}

async function handleGetId() {
	const fields = [id];
	if (fields.some((field) => field.value === "")) {
		alert("Vui lòng nhập đầy đủ thông tin");
		return;
	}
	await get_data();
}

await get_data();
</script>
<template>
	<SmallFormWrapper class="">
		<InputBox
			title="Nhập mã hộ gia đình"
			placeholder="Mã hộ gia đình"
			@update="id = $event.value"
		/>
		<button class="btn btn-primary w-full" @click="handleGetId()">
			Xem
		</button>
	</SmallFormWrapper>
	<RateTableView :data="res_data" />
</template>
