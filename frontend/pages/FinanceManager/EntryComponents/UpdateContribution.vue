<script setup lang="ts">
import ThreeInputFormWrapper from "../../../components/OneColFormWrapper.vue";
</script>

<template>
	<ThreeInputFormWrapper>
		<div class="w-full">
			<div class="mx-auto mb-2 w-full text-start">Mã đợt đóng góp</div>
			<input
				type="text"
				placeholder="Nhập mã đợt đóng góp"
				class="input input-bordered w-full"
			/>
		</div>
		<div class="w-full">
			<div class="mx-auto mb-2 w-full text-start">Tên đợt đóng góp</div>
			<input
				type="text"
				placeholder="Nhập tên đợt đóng góp"
				class="input input-bordered w-full"
			/>
		</div>
		<div class="w-full">
			<div class="mx-auto mb-2 w-full text-start">
				Tổng số tiền thu được
			</div>
			<input
				type="text"
				placeholder="Nhập số tiền"
				class="input input-bordered w-full"
			/>
		</div>
		<!--TODO: register handler -->
		<router-link to="/" class="w-full">
			<button class="btn btn-primary w-full">Cập nhật</button>
		</router-link>
	</ThreeInputFormWrapper>
</template>
