<script setup lang="ts">
import ThreeInputFormWrapper from "../../../components/OneColFormWrapper.vue";
import InputBox from "../../../components/InputBox.vue";
import { ref } from "vue";

const ssn = ref("");
const household_ssn = ref("");
const members = ref("");

const message = ref("");

function handleAddNewHousehold() {
	message.value = "";

	const fields = [ssn, household_ssn, members];

	if (!fields.every((field) => field.value)) {
		message.value = "Vui lòng điền đầy đủ thông tin";
		return;
	}
	// TODO: implement API
}
</script>

<template>
	<ThreeInputFormWrapper class="w-full">
		<InputBox
			title="Số hộ khẩu"
			placeholder="Nhập số hộ khẩu"
			@update="household_ssn = $event.value"
		/>
		<InputBox
			title="Số căn cước"
			placeholder="Nhập số căn cước"
			@update="ssn = $event.value"
		/>
		<InputBox
			title="Số căn cước các thành viên"
			placeholder="Mỗi số cách nhau bởi dấu phẩy"
			@update="members = $event.value"
		/>
		<button class="btn btn-primary w-full" @click="handleAddNewHousehold()">
			Tạo mới
		</button>
		<div v-if="message">{{ message }}</div>
	</ThreeInputFormWrapper>
</template>
