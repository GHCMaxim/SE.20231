<script setup lang="ts">
import ThreeInputFormWrapper from "../../../components/OneColFormWrapper.vue";
</script>

<template>
	<ThreeInputFormWrapper>
		<div class="w-full">
			<div class="mx-auto mb-2 w-full text-start">Số hộ khẩu</div>
			<input
				type="text"
				placeholder="Nhập số hộ khẩu"
				class="input input-bordered w-full"
			/>
		</div>
		<div class="w-full">
			<div class="mx-auto mb-2 w-full text-start">Số căn cước</div>
			<input
				type="text"
				placeholder="Nhập số căn cước của nhân khẩu qua đời"
				class="input input-bordered w-full"
			/>
		</div>
		<div class="w-full">
			<div class="mx-auto mb-2 w-full text-start">Lý do qua đời</div>
			<input
				type="text"
				placeholder="Tuổi già"
				class="input input-bordered w-full"
			/>
		</div>
		<!--TODO: register handler -->
		<router-link to="/" class="w-full">
			<button class="btn btn-primary w-full">Cập nhật</button>
		</router-link>
	</ThreeInputFormWrapper>
</template>
