<script setup lang="ts">
import OneColFormWrapper from "../../../components/OneColFormWrapper.vue";
import InputBox from "../../../components/InputBox.vue";
import { ref } from "vue";
import { API } from "../../../store";

const reward_type_id = ref("");
const reward_date = ref("");
const cccd = ref("");

const message = ref("");

async function handleCreate() {
	message.value = "";
	const fields = [reward_type_id, reward_date, cccd];

	if (!fields.every((field) => field.value)) {
		message.value = "Vui lòng điền đầy đủ thông tin";
		return;
	}

	const response = await fetch(API + "/api/rewards", {
		method: "POST",
		headers: {
			"Content-Type": "application/json",
			accept: "application/json",
		},
		body: JSON.stringify({
			reward_type_id: reward_type_id.value,
			date: reward_date.value,
			recipient: cccd.value,
			spending_id: 1,
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
	<OneColFormWrapper>
		<InputBox
			title="Điền mã loại phần thưởng"
			placeholder="1 - Phần thưởng cho học sinh / 2 - Phần thưởng đặc biệt"
			pattern = "[1-2]"
			@update="reward_type_id = $event.value"
		/>
		<InputBox
			title="Điền ngày nhận phần thưởng"
			placeholder="MM-DD-YYYY"
			@update="reward_date = $event.value"
			type="date"
		/>
		<InputBox
			title="Điền CCCD người nhận phần thưởng"
			placeholder="Nhập CCCD"
			@update="cccd = $event.value"
			pattern="\d{12}"
			warn="CCCD phải có 12 chữ số"
		/>
		<button class="btn btn-primary w-full" @click="handleCreate()">
			Tạo phần thưởng
		</button>
		<div v-if="message">{{ message }}</div>
	</OneColFormWrapper>
</template>
