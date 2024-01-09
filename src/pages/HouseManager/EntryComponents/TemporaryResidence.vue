<script setup lang="ts">
import ThreeInputFormWrapper from "../../../components/OneColFormWrapper.vue";
import InputBox from "../../../components/InputBox.vue";
import { ref } from "vue";
import { API } from "../../../store";

const household_ssn = ref("");
const ssn = ref("");
const move_out_reason = ref("");

const message = ref("");

async function handleMoveOut() {
	message.value = "";

	const fields = [ssn, household_ssn, move_out_reason];

	if (!fields.every((field) => field.value)) {
		message.value = "Vui lòng điền đầy đủ thông tin";
		return;
	}
	const response = await fetch(API + "/api/aways", {
		method: "POST",
		headers: {
			"Content-Type": "application/json",
			accept: "application/json",
		},
		body: JSON.stringify({
			household_id: household_ssn.value,
			cccd: ssn.value,
			away_type_id: 0,
			description: move_out_reason.value,
		}),
	});

	if (!response.ok) {
		message.value = response.statusText;
	} else {
		message.value = "Xử lý thành công";
	}
}
</script>

<template>
	<form @submit.prevent="handleMoveOut()">
	<ThreeInputFormWrapper>
		<InputBox
			title="Số hộ khẩu"
			placeholder="Nhập số hộ khẩu"
			type = "number"
			@update="household_ssn = $event.value"
		/>
		<InputBox
			title="Số căn cước"
			placeholder="Nhập số căn cước của nhân khẩu tạm trú, tạm vắng"
			pattern="\d{12}"
			warn="Số căn cước chỉ có 12 chữ số"
			@update="ssn = $event.value"
		/>
		<InputBox
			title="Lý do tạm trú/tạm vắng"
			placeholder="Đi học"
			@update="move_out_reason = $event.value"
		/>
		<button 
		type = "submit"
		class="btn btn-primary w-full">
			Cập nhật
		</button>
		<div v-if="message">{{ message }}</div>
	</ThreeInputFormWrapper>
	</form>
</template>
