<script setup lang="ts">
import NavigationBar from "../../components/NavigationBar.vue";
import SidebarEntry from "../../components/SidebarEntry.vue";
import Card from "./Card.vue";
import User from "./User.vue";
import { Ref, ref } from "vue";

const house_nums = ref("");
const people_nums = ref("");
const fund = ref("");
const fund_change = ref("");
const reward = ref("");

type User = {
	avatar: string;
	name: string;
	permissions: string;
}

const users: Ref<User[]> = ref([]);
async function handlePeopleNums() {
	const res = await fetch("http://localhost:8000/api/statistics/people");
	let data = await res.json();
	if (data === null || data === undefined || data === "") {
		data = 0;
	}
	people_nums.value = data;
}
async function handleFund() {
	const res = await fetch("http://localhost:8000/api/statistics/income");
	let data = await res.json();
	if (data === null || data === undefined || data === "") {
		data = [0, 0];
	}
	fund.value = (data[0] / 1000000).toString();
	fund_change.value = ((data[0] / data[1]) * 100).toString();
}
async function handleHouseNums() {
	const res = await fetch("http://localhost:8000/api/statistics/households");
	let data = await res.json();
	if (data === null || data === undefined || data === "") {
		data = 0;
	}
	house_nums.value = data;
}
async function handleReward() {
	const res = await fetch("http://localhost:8000/api/statistics/rewards");
	let data = await res.json();
	if (data === null || data === undefined || data === "") {
		data = 0;
	}
	reward.value = data;
}
async function handleUsers() {
	const res = await fetch("http://localhost:8000/api/users",
		{
			method: 'GET',
			headers: {
				'Content-Type': 'application/json',
				accept: 'application/json',
			},
		});
	try {
		const data = await res.json() as User[];
		users.value = data.map((user) => {
			return {
				avatar: "https://picsum.photos/200",
				name: user.name,
				permissions: user.permissions == "0" ? "Kế toán" : user.permissions == "1" ? "Ban quản lý" : user.permissions == "2" ? "Ban quản trị" : "",
			};
		});
	} catch (error) {
		console.error(error);
	}
}
Promise.all([
	handlePeopleNums(),
	handleFund(),
	handleHouseNums(),
	handleReward(),
	handleUsers(),
]);



</script>

<template>
	<NavigationBar />
	<div class="bg-slate-100">
		<SidebarEntry title="Trang chủ" icon="home" />
		<div
			class="mx-7 flex h-[calc(100vh-60px-160px-60px)] flex-row items-center justify-center gap-7 rounded-2xl border border-solid border-primary p-7">
			<div class="grid grid-cols-2 grid-rows-2 place-items-center justify-items-center gap-6">
				<Card>
					<div class="flex w-full flex-row items-center justify-between">
						<div>Tổng số hộ</div>
						<img src="/img/family.png" alt="family.png" class="h-12 w-auto" />
					</div>
					<div class="text-4xl font-semibold">{{ house_nums }}</div>
				</Card>
				<Card inverted>
					<div class="flex w-full flex-row items-center justify-between">
						<div class="text-black">Tổng số nhân khẩu</div>
						<img src="/img/human.png" alt="person.png" class="h-12 w-auto" />
					</div>
					<div class="text-4xl font-semibold">{{ people_nums }}</div>
				</Card>
				<Card inverted>
					<div class="flex w-full flex-row items-center justify-between">
						<div class="text-black">Quỹ đóng góp</div>
						<img src="/img/money.svg" alt="money.svg" class="h-12 w-auto" />
					</div>

					<div class="text-4xl">
						<sup>đ </sup>
						<span class="font-semibold">{{ fund }}</span>
						<span class="text-base"> triệu</span>
					</div>
					<div class="mt-2">
						<img src="/img/stonk.svg" alt="stonk.svg" class="inline-block h-3 w-auto" />
						Tăng {{ fund_change }}%
						<span class="text-black">so với cùng kỳ</span>
					</div>
				</Card>
				<Card>
					<div class="flex w-full flex-row items-center justify-between">
						<div>Khen thưởng</div>
						<img src="/img/gift.png" alt="gift.png" class="h-12 w-auto" />
					</div>
					<div class="text-4xl font-semibold">{{ reward }}</div>
					<div class="mt-2">phần quà trong năm 2023</div>
				</Card>
			</div>

			<div class="flex flex-col gap-4 rounded-2xl bg-white px-11 pb-8 pt-11">
				<div class="w-full text-start text-2xl">Ban quản trị</div>
				<div class="flex flex-col gap-5">
					<User v-for="user in users" :key="user.name" :avatar="user.avatar" :name="user.name"
						:permissions="user.permissions" />
				</div>
				<a href="#" class="mt-3 font-semibold text-primary">Hiện tất cả</a>
			</div>
		</div>
	</div>
</template>
