<script setup lang="ts">
import NavigationBar from "../components/NavigationBar.vue";
import SidebarEntry from "../components/SidebarEntry.vue";
</script>

<template>
	<NavigationBar />
	<div>
		<SidebarEntry title="Trang chủ" icon="home" />
		<div
			class="mx-7 h-[calc(100vh-60px-160px-60px)] rounded-2xl border border-solid border-primary p-7"
		>
			Placeholder
		</div>
	</div>
</template>
