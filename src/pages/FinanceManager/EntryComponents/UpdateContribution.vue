<script setup lang="ts">
import ThreeInputFormWrapper from "../../../components/OneColFormWrapper.vue";
import InputBox from "../../../components/InputBox.vue";
import { ref } from "vue";

const contribution_id = ref("");
const contribution_name = ref("");
const contribution_amount = ref("");

const message = ref("");

function handleUpdateContribution() {
	message.value = "";

	const fields = [contribution_id, contribution_name, contribution_amount];

	if (!fields.every((field) => field.value)) {
		message.value = "Vui lòng điền đầy đủ thông tin";
		return;
	}
	// TODO: implement put API
}
</script>

<template>
	<form @submit.prevent="handleUpdateContribution()">
	<ThreeInputFormWrapper>
		<InputBox
			title="Mã đợt đóng góp"
			placeholder="Nhập mã đợt đóng góp"
			@update="contribution_id = $event.value"
			type="number"
			warn="Mã đợt đóng góp chỉ bao gồm các chữ số"
		/>
		<InputBox
			title="Tên đợt đóng góp"
			placeholder="Nhập tên đợt đóng góp"
			@update="contribution_name = $event.value"
		/>
		<InputBox
			title="Tổng số tiền thu được"
			placeholder="Nhập số tiền"
			@update="contribution_amount = $event.value"
			type="number"
			warn="Số tiền chỉ bao gồm các chữ số"
		/>
		<button
			type = "submit"	
			class="btn btn-primary w-full"
		>
			Cập nhật
		</button>
		<div v-if="message">{{ message }}</div>
	</ThreeInputFormWrapper>
	</form>
</template>
