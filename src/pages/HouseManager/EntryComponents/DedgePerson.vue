<script setup lang="ts">
import ThreeInputFormWrapper from "../../../components/OneColFormWrapper.vue";
import InputBox from "../../../components/InputBox.vue";
import { ref } from "vue";
import { API } from "../../../store";

const household_ssn = ref("");
const ssn = ref("");
const deadge_reason = ref("");

const message = ref("");

async function handleDedgePerson() {
	message.value = "";

	const fields = [ssn, household_ssn, deadge_reason];

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
			away_type_id: 2,
			description: deadge_reason.value,
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
	<ThreeInputFormWrapper>
		<InputBox
			title="Số hộ khẩu"
			placeholder="Nhập số hộ khẩu"
			@update="household_ssn = $event.value"
			type="number"
		/>
		<InputBox
			title="Số căn cước"
			placeholder="Nhập số căn cước của nhân khẩu qua đời"
			pattern="^\d{12}$"
			warn="Số căn cước phải có 12 chữ số"
			@update="ssn = $event.value"
		/>
		<InputBox
			title="Lý do qua đời"
			placeholder="Tuổi già"
			@update="deadge_reason = $event.value"
		/>
		<button class="btn btn-primary w-full" @click="handleDedgePerson()">
			Cập nhật
		</button>
		<div v-if="message">{{ message }}</div>
	</ThreeInputFormWrapper>
</template>
