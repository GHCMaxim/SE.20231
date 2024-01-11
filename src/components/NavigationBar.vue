<script setup lang="ts">
import { inject } from "vue";
import router from "../router";
import type { VueCookies } from "vue-cookies";
import parseToken from "../parseToken";

const items = [
	["Thống kê", "chart-mixed", "/statistics"],
	["Tìm kiếm", "search", "/search"],
	// TODO: replace route
	["Thông báo", "bell", "/"],
];
const $cookies = inject<VueCookies>("$cookies");
const userName = parseToken()?.name ?? "Người dùng";
const avatar = "https://picsum.photos/200";
const currentRoute = router.currentRoute.value.path;
function logout() {
	// clear cookies
	$cookies!.remove("token");
	router.push("/login");
}
</script>

<template>
	<div class="sticky top-0">
		<div
			class="flex h-16 w-full flex-row items-center justify-between px-5"
		>
			<button class="btn btn-ghost" @click="logout">Đăng xuất</button>

			<div class="flex flex-row items-center gap-10">
				<router-link
					v-for="item in items"
					:key="item[0]"
					class="flex h-full flex-row items-center justify-center gap-3 font-semibold text-primary/90 transition-all hover:text-primary"
					:to="item[2]"
				>
					<i :class="`fa-light fa-${item[1]}`" />
					<div>{{ item[0] }}</div>
				</router-link>
				<div class="flex items-center justify-center gap-4">
					<div>{{ userName }}</div>
					<img :src="avatar" alt="avatar" class="h-10 rounded-full" />
				</div>
			</div>
		</div>

		<div
			class="flex h-24 flex-row items-center justify-between bg-primary px-5 py-2"
		>
			<router-link to="/" class="h-full">
				<img
					src="../assets/logo.png"
					alt="logo"
					class="h-full w-auto"
				/>
			</router-link>

			<router-link
				to="/"
				class="text-2xl font-bold uppercase transition-all hover:text-white"
				:class="currentRoute === '/' ? 'text-white' : 'text-white/75'"
			>
				trang chủ
			</router-link>
			<router-link
				to="/household-manager"
				class="text-base font-bold uppercase transition-all hover:text-white"
				:class="
					currentRoute === '/household-manager'
						? 'text-white'
						: 'text-white/75'
				"
			>
				quản lý hộ khẩu,<br />nhân khẩu
			</router-link>
			<router-link
				to="/finance-manager"
				class="text-base font-bold uppercase transition-all hover:text-white"
				:class="
					currentRoute === '/finance-manager'
						? 'text-white'
						: 'text-white/75'
				"
			>
				quản lý thu phí,<br />đóng góp
			</router-link>
			<router-link
				to="/rewards"
				class="text-base font-bold uppercase transition-all hover:text-white"
				:class="
					currentRoute === '/rewards' ? 'text-white' : 'text-white/75'
				"
			>
				quản lý<br />khen thưởng
			</router-link>

			<div class="hidden lg:block" />
		</div>
	</div>
</template>
