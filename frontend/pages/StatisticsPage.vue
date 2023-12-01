<script setup lang="ts">
import SidebarEntry from "../components/SidebarEntry.vue";
import NavigationBar from "../components/NavigationBar.vue";
import RightSideContainer from "../components/RightSideContainer.vue";
</script>

<template>
	<NavigationBar />
	<div class="flex flex-row">
		<div>
			<SidebarEntry title="Thống kê" icon="chart-mixed" />
			<div class="px-10">
				<div class="mb-3 text-left">Thống kê theo</div>
				<select class="select select-bordered mb-5 w-full">
					<option selected>Độ tuổi</option>
				</select>
				<button class="btn btn-primary w-full">Tìm</button>
			</div>
		</div>
		<RightSideContainer> Statistics placeholder </RightSideContainer>
	</div>
</template>
