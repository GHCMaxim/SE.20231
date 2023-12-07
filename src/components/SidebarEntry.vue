<script setup lang="ts">
const props = defineProps({
	title: {
		type: String,
		required: true,
	},
	icon: {
		type: String,
		default: "",
	},
});
</script>

<template>
	<div
		class="my-5 flex w-[300px] items-center justify-center gap-3 rounded-r-full bg-primary py-4 text-center text-lg font-bold uppercase text-white"
	>
		<i v-if="props.icon" :class="`fa-light fa-${props.icon}`" />
		{{ props.title }}
	</div>
</template>
