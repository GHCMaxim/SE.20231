<script setup lang="ts">
import { ref } from "vue";
import { API } from "../../../store";
import InputBox from "../../../components/InputBox.vue";

const ssn = ref("");
const ethnicity = ref("");
const religion = ref("");
const name = ref("");
const sex = ref("");
const job = ref("");
const dob = ref("");
const phone = ref("");
const workplace = ref("");

const message = ref("");

async function handleAddNewPerson() {
	message.value = "";
	console.log(sex.value);
	const fields = [
		ssn,
		ethnicity,
		religion,
		name,
		sex,
		job,
		dob,
		phone,
		workplace,
	];

	if (!fields.every((field) => field.value)) {
		message.value = "Vui lòng điền đầy đủ thông tin";
		return;
	}

	if (sex.value === "Nữ") {
		sex.value = "F";
	} else {
		sex.value = "M";
	}
	const response = await fetch(API + "/api/people", {
		method: "POST",
		headers: {
			"Content-Type": "application/json",
			accept: "application/json",
		},
		body: JSON.stringify({
			name: name.value,
			dob: dob.value,
			sex: sex.value,
			religion: religion.value,
			ethnicity: ethnicity.value,
			job: job.value,
			job_location: workplace.value,
			cccd: ssn.value,
			phone_number: phone.value,
		}),
	});

	if (!response.ok) {
		message.value = response.statusText;
	} else {
		message.value = "Đăng ký thành công";
	}
}
</script>
<template>
	<div class="flex h-full flex-col items-center justify-center gap-3">
		<form @submit.prevent="handleAddNewPerson()">
			<div
				class="mx-auto mb-10 mt-8 grid w-4/5 max-w-2xl grid-cols-2 grid-rows-4 gap-x-10 gap-y-7"
			>
				<InputBox
					title="Số căn cước"
					placeholder="Nhập số căn cước"
					pattern="\d{12}"
					warn="Mã căn cước phải có 12 chữ số"
					@update="ssn = $event.value"
				/>
				<div class="grid grid-cols-2 flex-row gap-3">
					<InputBox
						title="Dân tộc"
						placeholder="Kinh"
						@update="ethnicity = $event.value"
					/>
					<InputBox
						title="Tôn giáo"
						placeholder="Không"
						@update="religion = $event.value"
					/>
				</div>
				<InputBox
					title="Họ tên"
					placeholder="Nguyễn Văn A"
					@update="name = $event.value"
				/>
				<div>
					<div class="mx-auto mb-2 text-start">Giới tính</div>
					<select v-model="sex" class="select select-bordered w-full">
						<option disabled selected value="">
							Chọn giới tính
						</option>
						<option value="Nam">Nam</option>
						<option value="Nữ">Nữ</option>
					</select>
				</div>
				<InputBox
					title="Nghề nghiệp"
					placeholder="Kế toán"
					@update="job = $event.value"
				/>
				<InputBox
					title="Ngày sinh"
					placeholder="Nhập ngày sinh"
					type="date"
					@update="dob = $event.value"
				/>
				<InputBox
					title="Số điện thoại"
					placeholder="0123456789"
					pattern="\d{10}"
					warn="Số điện thoại phải có 10 chữ số"
					@update="phone = $event.value"
				/>
				<InputBox
					title="Nơi làm việc"
					placeholder="Số 1, Đại Cồ Việt, Hai Bà Trưng, Hà Nội"
					@update="workplace = $event.value"
				/>
			</div>
			<button type="submit" class="btn btn-primary w-80 self-center">
				Đăng ký
			</button>
		</form>

		<div v-if="message">{{ message }}</div>
	</div>
</template>
