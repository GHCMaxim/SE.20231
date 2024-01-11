<script setup lang="ts">
import OneColFormWrapper from "../../../components/OneColFormWrapper.vue";
import InputBox from "../../../components/InputBox.vue";
import { ref } from "vue";
import { API } from "../../../store";

const contributor = ref("");
const id = ref("");
const amount = ref("");
const description = ref("");
const contribution_date = ref("");
const contribution_event = ref("");
const message = ref("");

async function handleAddNewContribution() {
    message.value = "";
    id.value = "0";
    const fields = [
        id,
        contributor,
        amount,
        description,
        contribution_date,
        contribution_event,
    ];
    if (!fields.every((field) => field.value)) {
        message.value = "Vui lòng điền đầy đủ thông tin";
        return;
    }

    const response = await fetch(API + "/api/relationships", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            accept: "application/json",
        },
        body: JSON.stringify({
            id: id.value,
            contributor: contributor.value,
            amount: parseInt(amount.value),
            description: description.value,
            contribution_date: contribution_date.value,
            contribution_event: parseInt(contribution_event.value),
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
    <form @submit.prevent="handleAddNewContribution()">
        <OneColFormWrapper class="w-full">
            <InputBox title="Số căn cước công dân người đóng góp" placeholder="CCCD" pattern="\d{12}"
                warn="Số CCCD phải là 12 chữ số" @update="contributor = $event.value" />
            <InputBox title="Lượng đóng góp" placeholder="100000" type="number" @update="amount = $event.value" />
            <InputBox title="Nội dung đóng góp" placeholder="Đóng cho ..." @update="description = $event.value" />
            <InputBox title="Ngày đóng góp" placeholder="2021-10-10" type="date"
                @update="contribution_date = $event.value" />
            <InputBox title="Mã sự kiện đóng góp" placeholder="10" type="number"
                @update="contribution_event = $event.value" />
            <button type="submit" class="btn btn-primary w-full">
                Tạo mới
            </button>
            <div v-if="message">{{ message }}</div>
        </OneColFormWrapper>
    </form>
</template>
