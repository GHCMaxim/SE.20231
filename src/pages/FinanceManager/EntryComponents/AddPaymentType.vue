<script setup lang="ts">
import OneColFormWrapper from "../../../components/OneColFormWrapper.vue";
import InputBox from "../../../components/InputBox.vue";
import { ref } from "vue";
import { API } from "../../../store";

const household_ssn = ref("");
const name = ref("");
const creation_date = ref("");
const location = ref("");
const owner = ref("");

const message = ref("");

async function handleAddNewHousehold() {
	message.value = "";

	const fields = [household_ssn, location, owner, name, creation_date];
	if (!fields.every((field) => field.value)) {
		message.value = "Vui lòng điền đầy đủ thông tin";
		return;
	}

	const response = await fetch(API + "api/household", {
		method: "POST",
		headers: {
			"Content-Type": "application/json",
			accept: "application/json",
		},
		body: JSON.stringify({
			id: household_ssn.value,
			name: name.value,
			location: location.value,
			creation_date: creation_date.value,
			owner: owner.value,
		}),
	});
	if (!response.ok) {
		message.value = response.statusText;
	} else {
		message.value = "Tạo mới thành công";
	}
}
</script>

<template>
	<form @submit.prevent="handleAddNewHousehold()">
		<OneColFormWrapper class="w-full">
			<InputBox
				title="Số hộ khẩu"
				placeholder="Nhập số hộ khẩu"
				type="number"
				warn="Số sổ hộ khẩu chỉ có số"
				@update="household_ssn = $event.value"
			/>
			<InputBox
				title="Số tên căn hộ"
				placeholder="N02-1810"
				@update="name = $event.value"
			/>
			<InputBox
				title="Số địa chỉ hộ khẩu"
				placeholder="Nhập địa chỉ"
				@update="location = $event.value"
			/>
			<InputBox
				title="Số căn cước chủ hộ khẩu"
				placeholder="Nhập số căn cước"
				type="number"
				warn="Số căn cước chỉ có số"
				@update="owner = $event.value"
			/>
			<InputBox
				title="Số ngày thành lập sổ hộ khẩu"
				placeholder="DD/MM/YYYY"
				type="date"
				@update="creation_date = $event.value"
			/>

			<button class="btn btn-primary w-full">Tạo mới</button>
			<div v-if="message">{{ message }}</div>
		</OneColFormWrapper>
	</form>
</template>
