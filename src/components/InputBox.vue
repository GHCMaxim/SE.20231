<script setup lang="ts">
defineEmits(["update"]);
const props = defineProps({
	title: {
		type: String,
		default: "",
	},
	placeholder: {
		type: String,
		default: "",
	},
	pattern: {
		type: String,
		default: ".*",
	},
	warn: {
		type: String,
		default: "",
	},
	type: {
		type: String,
		default: "text",
	},
});
</script>

<template>
	<div class="w-full">
		<div class="mx-auto mb-2 text-start">{{ props.title }}</div>
		<input
			:type="props.type"
			:placeholder="props.placeholder"
			class="input input-bordered w-full"
			:pattern="props.pattern"
			:title="props.warn"
			@input="$emit('update', $event.target)"
		/>
	</div>
</template>
