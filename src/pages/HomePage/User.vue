<script setup lang="ts">
const props = defineProps({
	avatar: {
		type: String,
		default: "https://picsum.photos/200",
	},
	name: {
		type: String,
		default: "Nguyễn Văn A",
	},
	role: {
		type: String,
		default: "Nhân viên",
	},
});
</script>

<template>
	<div class="flex flex-row gap-3">
		<img :src="props.avatar" class="h-12 w-12 rounded-full object-cover" />
		<div class="flex flex-col items-start justify-between">
			<div class="font-bold">{{ props.name }}</div>
			<div>{{ props.role }}</div>
		</div>
	</div>
</template>
