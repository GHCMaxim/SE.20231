<script setup lang="ts">
defineEmits(["update"]);
defineProps({
	title: {
		type: String,
		default: "",
	},
	placeholder: {
		type: String,
		default: "",
	},
});
</script>

<template>
	<div class="w-full">
		<div class="mx-auto mb-2 text-start">{{ title }}</div>
		<input
			type="text"
			:placeholder="placeholder"
			class="input input-bordered w-full"
			@input="$emit('update', $event.target)"
		/>
	</div>
</template>
