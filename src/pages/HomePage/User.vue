<script setup lang="ts">
const props = defineProps({
	avatar: {
		type: String,
		required: true,
	},
	name: {
		type: String,
		required: true,
	},
	permissions: {
		type: String,
		required: true,
	},
});
</script>

<template>
	<div class="flex flex-row gap-3">
		<img :src="props.avatar" class="h-12 w-12 rounded-full object-cover" />
		<div class="flex flex-col items-start justify-between">
			<div class="font-bold">{{ props.name }}</div>
			<div>{{ props.permissions }}</div>
		</div>
	</div>
</template>
