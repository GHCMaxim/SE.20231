<script setup lang="ts">
import InputBox from "../../../components/InputBox.vue";
import { ref } from "vue";
import { API } from "../../../store";

const household_ssn = ref("");
const name = ref("");
const creation_date = ref("");
const location = ref("");
const owner = ref("");
const house_type = ref("");
const house_size = ref("");

const message = ref("");

async function handleAddNewHousehold() {
	message.value = "";

	const fields = [household_ssn, location, owner, name, creation_date];
	if (!fields.every((field) => field.value)) {
		message.value = "Vui lòng điền đầy đủ thông tin";
		return;
	}


	const response = await fetch(API + "/api/household_registrations", {
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
			size: house_size.value,
			house_type: house_type.value,
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
		<div class="mx-auto mb-10 mt-8 grid w-4/5 max-w-2xl grid-cols-2 gap-x-10 gap-y-7">
			<InputBox title="Số hộ khẩu" placeholder="Nhập số hộ khẩu" @update="household_ssn = $event.value" type="number"
				warn="Số sổ hộ khẩu chỉ có số" />
			<InputBox title="Tên căn hộ" placeholder="N02-1810" @update="name = $event.value" />
			<InputBox title="Số căn cước chủ hộ khẩu" placeholder="Nhập số căn cước" @update="owner = $event.value"
				type="number" warn="Số căn cước chỉ có số" />
			<InputBox title="Số ngày thành lập sổ hộ khẩu" placeholder="DD/MM/YYYY" @update="creation_date = $event.value"
				type="date" />
			<div>
				<div class="mx-auto mb-2 text-start">Loại căn hộ</div>
				<select v-model="house_type" class="select select-bordered w-full">
					<option disabled selected value="">Chọn loại chung cư</option>
					<option value="1">Chung cư giá rẻ </option>
					<option value="2">Chung cư thường</option>
					<option value="3">Chung cư cao cấp</option>
				</select>
			</div>
			<InputBox title="Diện tích căn hộ (m2)" placeholder="Nhập diện tích" @update="house_size = $event.value"
				type="number" warn="Diện tích chỉ có số" />

			<div class="mx-auto flex h-full w-full max-w-2xl flex-col items-center justify-center col-span-2">
				<div class="mb-2 text-start w-full">Địa chỉ</div>
				<input type="text" placeholder="Nhập địa chỉ" class="input input-bordered w-full mb-4"
					@update="location = $event.value" />
				<button type="submit" class="btn btn-primary w-80 self-center">
					Tạo mới
				</button>
			</div>
		</div>
		<div v-if="message">{{ message }}</div>

	</form>
</template>
