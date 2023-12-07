<script setup lang="ts">
import ThreeInputFormWrapper from "../../../components/OneColFormWrapper.vue";
import InputBox from "../../../components/InputBox.vue";
import { ref } from "vue";

const household_ssn = ref("");
const ssn = ref("");
const deadge_reason = ref("");

const message = ref("");

function handleDedgePerson() {
	message.value = "";

	const fields = [ssn, household_ssn, deadge_reason];

	if (!fields.every((field) => field.value)) {
		message.value = "Vui lòng điền đầy đủ thông tin";
		return;
	}
	// TODO: implement API
}
</script>

<template>
	<ThreeInputFormWrapper>
		<InputBox
			title="Số hộ khẩu"
			placeholder="Nhập số hộ khẩu"
			@update="household_ssn = $event.value"
		/>
		<InputBox
			title="Số căn cước"
			placeholder="Nhập số căn cước của nhân khẩu qua đời"
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
