<script setup lang="ts">
import OneColFormWrapper from "../../../components/OneColFormWrapper.vue";
import InputBox from "../../../components/InputBox.vue";
import { ref } from "vue";
import { API } from "../../../store";

const id = ref("");
const description = ref("");
const event_time = ref("");

const message = ref("");

async function handleAddNewContributionEvent() {
    message.value = "";

    const fields = [
        id,
        description,
        event_time,
    ];
    if (!fields.every((field) => field.value)) {
        message.value = "Vui lòng điền đầy đủ thông tin";
        return;
    }

    const response = await fetch(API + "/api/contribution_events", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            accept: "application/json",
        },
        body: JSON.stringify({
            id: id.value,
            total_amount: 0,
            description: description.value,
            event_time: event_time.value,
        }),
    });
    if (!response.ok) {
        message.value = response.statusText;
    } else {
        message.value = "Tạo mới thành công";
    }
}
</script>

<template>
    <form @submit.prevent="handleAddNewContributionEvent()">
        <OneColFormWrapper class="w-full">
            <InputBox title="Mã đợt đóng góp" placeholder="Mã đợt" type="number" @update="id = $event.value" />
            <InputBox title="Tên đợt đóng góp" placeholder="Hỗ trợ người nghèo" @update="description = $event.value" />
            <InputBox title="Thời gian bắt đầu đóng góp" placeholder="2021-10-10" type="date"
                @update="event_time = $event.value" />

            <button type="submit" class="btn btn-primary w-full">
                Tạo mới
            </button>
            <div v-if="message">{{ message }}</div>
        </OneColFormWrapper>
    </form>
</template>
