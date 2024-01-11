<script setup lang="ts">
import { ref, inject } from "vue";
import type { VueCookies } from "vue-cookies";
import { API } from "../store";
import router from "../router";

function forgot_password() {
	alert("Liên hệ admin để lấy lại mật khẩu");
}

const username = ref("");
const password = ref("");

const message = ref("");
const $cookies = inject<VueCookies>("$cookies");
async function login() {
	const formData = new URLSearchParams();
	formData.append("username", username.value);
	formData.append("password", password.value);
	const response = await fetch(API + "/api/login", {
		method: "POST",
		body: formData,
	});

	if (!response.ok) {
		message.value = response.statusText;
		if (message.value == "Unprocessable Entity") {
			message.value = "Thiếu tên đăng nhập hoặc mật khẩu";
		} else if (message.value == "Not Found") {
			message.value = "Tài khoản hoặc mật khẩu sai";
		} else if (message.value == "Unauthorized") {
			message.value = "Tài khoản hoặc mật khẩu sai";
		}
		return;
	}
	const token = await response.json().then((resp) => resp.access_token);
	$cookies!.set("token", token);
	router.push("/");

}
</script>

<template>
	<div class="grid h-screen w-full grid-cols-[1fr_600px]">
		<img src="../assets/login-bg.png" alt="login-bg" class="h-full max-h-screen w-full object-cover" />
		<div class="mt-16 flex flex-col items-center justify-start gap-6">
			<img src="../assets/logo.png" alt="logo" class="h-auto w-80 rounded-xl bg-primary px-5 py-3" />
			<form @submit.prevent="login()">
				<div class="flex w-80 flex-col items-start">
					<div class="mb-2 justify-items-start text-lg">Tài khoản</div>
					<input require v-model="username" type="text" placeholder="Nhập tài khoản"
						class="input input-bordered w-full max-w-xs" />
				</div>

				<div class="flex w-80 flex-col items-start">
					<div class="mb-2 justify-items-start text-lg">Mật khẩu</div>
					<input require v-model="password" type="password" placeholder="Nhập mật khẩu"
						class="input input-bordered w-full max-w-xs" />
				</div>

				<div class="flex w-80 justify-end">
					<button class="m-0 w-fit border-none bg-transparent p-0 text-end active:outline-none"
						@click="forgot_password()">
						Quên mật khẩu?
					</button>
				</div>

				<button type="submit" class="btn btn-primary w-80">
					Đăng nhập
				</button>
			</form>
			<div class="w-80">
				Chưa có tài khoản?
				<router-link to="/register">Đăng ký</router-link>
			</div>
			<div class="w-80 text-red-500">{{ message }}</div>
		</div>
	</div>
</template>
