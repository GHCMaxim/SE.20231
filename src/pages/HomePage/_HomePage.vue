<script setup lang="ts">
import NavigationBar from "../../components/NavigationBar.vue";
import SidebarEntry from "../../components/SidebarEntry.vue";
import Card from "./Card.vue";
import User from "./User.vue";
</script>

<template>
	<NavigationBar />
	<div class="bg-slate-100">
		<SidebarEntry title="Trang chủ" icon="home" />
		<div
			class="mx-7 flex h-[calc(100vh-60px-160px-60px)] flex-row items-center justify-center gap-7 rounded-2xl border border-solid border-primary p-7">
			<div
				class="grid grid-cols-2 grid-rows-2 place-items-center justify-items-center gap-6">
				<Card>
					<div
						class="flex w-full flex-row items-center justify-between">
						<div>Tổng số hộ</div>
						<img
							src="/img/family.png"
							alt="family.png"
							class="h-12 w-auto" />
					</div>
					<div class="text-4xl font-semibold">1.000</div>
				</Card>
				<Card inverted>
					<div
						class="flex w-full flex-row items-center justify-between">
						<div class="text-black">Tổng số nhân khẩu</div>
						<img
							src="/img/human.png"
							alt="person.png"
							class="h-12 w-auto" />
					</div>
					<div class="text-4xl font-semibold">3.000</div>
				</Card>
				<Card inverted>
					<div
						class="flex w-full flex-row items-center justify-between">
						<div class="text-black">Quỹ đóng góp</div>
						<img
							src="/img/money.svg"
							alt="money.svg"
							class="h-12 w-auto" />
					</div>

					<div class="text-4xl">
						<sup>đ </sup>
						<span class="font-semibold">2.50</span>
						<span class="text-base"> triệu</span>
					</div>
					<div class="mt-2">
						<img
							src="/img/stonk.svg"
							alt="stonk.svg"
							class="inline-block h-3 w-auto" />
						Tăng 5%
						<span class="text-black">so với cùng kỳ</span>
					</div>
				</Card>
				<Card>
					<div
						class="flex w-full flex-row items-center justify-between">
						<div>Khen thưởng</div>
						<img
							src="/img/gift.png"
							alt="gift.png"
							class="h-12 w-auto" />
					</div>
					<div class="text-4xl font-semibold">123.456</div>
					<div class="mt-2">phần quà trong năm 2023</div>
				</Card>
			</div>

			<div class="flex flex-col gap-4 rounded-2xl bg-white px-11 pt-11 pb-8">
				<div class="text-2xl w-full text-start">Ban quản trị</div>
				<div class="flex flex-col gap-5">
					<User />
					<User />
					<User />
				</div>
				<a href="#" class="text-primary mt-3 font-semibold">Hiện tất cả</a>
			</div>
		</div>
	</div>
</template>
