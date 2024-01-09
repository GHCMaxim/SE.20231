<script setup lang="ts">
import OneColFormWrapper from "../../../components/OneColFormWrapper.vue";
import InputBox from "../../../components/InputBox.vue";
import { ref } from "vue";
import { API } from "../../../store";

const cccd = ref("");
const relationship = ref("");
const household_id = ref("");

const message = ref("");

async function handleAddNewHousehold() {
	message.value = "";

	const fields = [household_id, relationship, cccd];
	if (!fields.every((field) => field.value)) {
		message.value = "Vui lòng điền đầy đủ thông tin";
		return;
	}

	const response = await fetch(API + "/api/relationships", {
		method: "POST",
		headers: {
			"Content-Type": "application/json",
			accept: "application/json",
		},
		body: JSON.stringify({
			cccd: cccd.value,
			relationship: relationship.value,
			birth_id: null,
			alive: "true",
			death_paper_id: null,
			household_id: household_id.value,
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
			title="Số căn cước công dân"
			placeholder="CCCD"
			pattern ="\d{12}"
			warn = "Số CCCD phải là 12 chữ số"
			@update="cccd = $event.value"
		/>
		<InputBox
			title="Mối quan hệ với chủ hộ"
			placeholder="Con trai / Bố / Mẹ"
			@update="relationship = $event.value"
		/>
		<InputBox
			title="Số hộ khẩu"
			placeholder="Nhập số hộ khẩu"
			type="number"
			warn="Số hộ khẩu phải là số"
			@update="household_id = $event.value"
		/>

		<button 
			type = "submit"
			class="btn btn-primary w-full" >
			Tạo mới
		</button>
		<div v-if="message">{{ message }}</div>
	</OneColFormWrapper>
	</form>
</template>
