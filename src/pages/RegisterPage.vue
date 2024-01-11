<script setup lang="ts">
import { ref } from "vue";
import { useRouter } from "vue-router";
import { API } from "../store";

const username = ref("");
const password = ref("");
const name = ref("");
const sex = ref("");
const dob = ref("");
const cccd = ref("");
const address = ref("");
const permissions = ref("");

const message = ref("");

async function register() {
	if (
		!username.value ||
		!password.value ||
		!name.value ||
		!sex.value ||
		!dob.value ||
		!cccd.value ||
		!address.value
	) {
		message.value = "Bạn cần phải điền tất cả các trường!";
	} else {
		const body = {
			username: username.value,
			password: password.value,
			name: name.value,
			sex: sex.value == "Nam" ? "M" : "F",
			address: address.value,
			cccd: cccd.value,
			permissions:
				permissions.value == "Kế toán"
					? 0
					: permissions.value == "Ban quản lý"
						? 1
						: 2,
			job: permissions.value,
		};

		const response = await fetch(API + "/api/users", {
			method: "POST",
			headers: {
				"Content-Type": "application/json",
				accept: "application/json",
			},
			body: JSON.stringify(body),
		});

		if (!response.ok) {
			message.value = response.statusText;
		} else {
			alert("Đăng ký thành công!");
			useRouter().push("/login");
		}
	}
}
</script>

<template>
	<div class="grid grid-cols-[0fr_1fr] xl:grid-cols-[1fr_2fr]">
		<div
			class="flex h-screen w-full items-center justify-center overflow-hidden"
		>
			<img
				src="../assets/logo.png"
				alt="logo"
				class="h-auto w-96 rounded-xl bg-primary object-cover px-5 py-3"
			/>
		</div>

		<div class="mt-12 flex flex-col gap-3 px-5">
			<div class="text-5xl font-bold">Tạo tài khoản mới</div>
			<div class="text-xl">
				Đã có tài khoản?
				<router-link to="/login"> Đăng nhập </router-link>
			</div>
			<form @submit.prevent="register()">
				<div
					class="mx-10 mb-12 mt-8 grid grid-cols-2 grid-rows-4 gap-x-10 gap-y-7"
				>
					<div>
						<div class="mx-auto mb-2 text-start">Tài khoản</div>
						<input
							v-model="username"
							type="text"
							placeholder="Nhập tài khoản"
							class="input input-bordered w-full"
						/>
					</div>
					<div>
						<div class="mx-auto mb-2 text-start">Mật khẩu</div>
						<input
							v-model="password"
							type="password"
							placeholder="Nhập mật khẩu"
							class="input input-bordered w-full"
						/>
					</div>
					<div>
						<div class="mx-auto mb-2 text-start">Họ tên</div>
						<input
							v-model="name"
							type="text"
							placeholder="Nguyễn Văn A"
							class="input input-bordered w-full"
						/>
					</div>
					<div>
						<div class="mx-auto mb-2 text-start">Giới tính</div>
						<select
							v-model="sex"
							class="select select-bordered w-full"
						>
							<option disabled selected>Chọn giới tính</option>
							<option>Nam</option>
							<option>Nữ</option>
						</select>
					</div>
					<div>
						<div class="mx-auto mb-2 text-start">Chức vụ</div>
						<select
							v-model="permissions"
							class="select select-bordered w-full"
						>
							<option disabled selected>Chọn chức vụ</option>
							<option>Kế toán</option>
							<option>Ban quản lý</option>
							<option>Ban quản trị</option>
						</select>
					</div>
					<div>
						<div class="mx-auto mb-2 text-start">Ngày sinh</div>
						<input
							v-model="dob"
							type="date"
							placeholder="Nhập ngày sinh"
							class="input input-bordered w-full"
						/>
					</div>
					<div>
						<div class="mx-auto mb-2 text-start">CCCD</div>
						<input
							v-model="cccd"
							type="text"
							placeholder="0123456789"
							class="input input-bordered w-full"
							pattern="\d{12}"
							title="CCCD phải có 12 chữ số"
						/>
					</div>
					<div>
						<div class="mx-auto mb-2 text-start">Địa chỉ</div>
						<input
							v-model="address"
							type="text"
							placeholder="Số 1, Đại Cồ Việt, Hai Bà Trưng, Hà Nội"
							class="input input-bordered w-full"
						/>
					</div>
				</div>

				<!-- TODO: register handler -->
				<button type="submit" class="btn btn-primary w-80">
					Đăng ký
				</button>
				<div v-if="message">{{ message }}</div>
				<div v-if="message === 'Đăng ký thành công!'">
					<router-link to="/login"> Đăng nhập </router-link>
				</div>
			</form>
		</div>
	</div>
	Register page
</template>
