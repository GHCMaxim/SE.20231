<script setup lang="ts">
import { ref, inject } from "vue";
import type { VueCookies } from "vue-cookies";
import { API } from "../store";

function forgot_password() {
	alert("Liên hệ admin để lấy lại mật khẩu");
}

const username = ref("");
const password = ref("");

const message = ref("");

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
	} else {
		const token = await response.json().then(resp => resp.access_token);
		const $cookies = inject<VueCookies>("$cookies");
		$cookies!.set("token", token);
	}
}
</script>


<template>
	<div class="grid h-screen w-full grid-cols-[1fr_600px]">
		<img
			src="../assets/login-bg.png"
			alt="login-bg"
			class="h-full max-h-screen w-full object-cover"
		/>
		<div class="mt-16 flex flex-col items-center justify-start gap-6">
			<img
				src="../assets/logo.png"
				alt="logo"
				class="h-auto w-80 rounded-xl bg-primary px-5 py-3"
			/>

			<div class="flex w-80 flex-col items-start">
				<div class="mb-2 justify-items-start text-lg">Tài khoản</div>
				<input
					type="text"
					placeholder="Nhập tài khoản"
					v-model="username"
					class="input input-bordered w-full max-w-xs"
				/>
			</div>

			<div class="flex w-80 flex-col items-start">
				<div class="mb-2 justify-items-start text-lg">Mật khẩu</div>
				<input
					type="password"
					placeholder="Nhập mật khẩu"
					v-model="password"
					class="input input-bordered w-full max-w-xs"
				/>
			</div>

			<div class="flex w-80 justify-end">
				<button
					class="m-0 w-fit border-none bg-transparent p-0 text-end active:outline-none"
					@click="forgot_password()"
				>
					Quên mật khẩu?
				</button>
			</div>

			<!-- TODO: login handler -->
			<router-link to="/">
				<button class="btn btn-primary w-80" @click="login()">Đăng nhập</button>
			</router-link>

			<div class="w-80">
				Chưa có tài khoản?
				<router-link to="/register">Đăng ký</router-link>
			</div>
		</div>
	</div>
</template>
