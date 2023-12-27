<script setup lang="ts">
defineProps({
	inverted: {
		type: Boolean,
		default: false,
	},
});
</script>

<template>
	<div
		class="flex h-40 w-[260px] flex-col items-start justify-start gap-1 rounded-2xl p-5"
		:class="{
			'bg-white text-primary': inverted,
			'bg-primary text-white': !inverted,
		}"
	>
		<slot />
	</div>
</template>
