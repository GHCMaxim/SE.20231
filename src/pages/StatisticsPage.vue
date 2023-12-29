<script setup lang="ts">
import SidebarEntry from "../components/SidebarEntry.vue";
import NavigationBar from "../components/NavigationBar.vue";
import RightSideContainer from "../components/RightSideContainer.vue";
import PieChartAge from "../components/PieChartAge.vue";
import PieChartSegs from "../components/PieChartSegs.vue";
import { ref } from "vue";
const currentEntryRef = ref("");
</script>

<template>
	<NavigationBar />
	<div class="flex flex-row">
		<div>
			<SidebarEntry title="Thống kê" icon="chart-mixed" />
			<div class="px-10">
				<div class="mb-3 text-left">Thống kê theo</div>
				<select
					v-model="currentEntryRef"
					class="select select-bordered mb-5 w-full"
				>
					<option selected>Độ tuổi</option>
					<option>Giới tính</option>
				</select>
				<button class="btn btn-primary w-full">Tìm</button>
			</div>
		</div>
		<RightSideContainer>
			<div
				v-if="currentEntryRef === 'Độ tuổi'"
				class="flex flex-col items-center"
			>
				<div class="mb-5 text-2xl font-bold">Thống kê theo độ tuổi</div>
				<Suspense>
					<PieChartAge />
				</Suspense>
			</div>
			<div
				v-if="currentEntryRef === 'Giới tính'"
				class="flex flex-col items-center"
			>
				<div class="mb-5 text-2xl font-bold">
					Thống kê theo giới tính
				</div>
				<Suspense>
					<PieChartSegs />
				</Suspense>
			</div>
		</RightSideContainer>
	</div>
</template>
