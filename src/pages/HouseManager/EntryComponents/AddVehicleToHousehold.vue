<script setup lang="ts">
import OneColFormWrapper from "../../../components/OneColFormWrapper.vue";
import InputBox from "../../../components/InputBox.vue";
import { ref } from "vue";
import { API } from "../../../store";

const household_id = ref("");
const license_plate = ref("");
const vehicle_type = ref("");

const message = ref("");

async function handleAddNewVehicle(){
    message.value = "";

    const fields = [household_id, license_plate, vehicle_type];
    if (!fields.every((field) => field.value)) {
        message.value = "Vui lòng điền đầy đủ thông tin";
        return;
    }

    const response = await fetch(API + "/api/vehicles", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            accept: "application/json",
        },
        body: JSON.stringify({
            license_plate: license_plate.value,
            vehicle_type: vehicle_type.value,
            owner: household_id.value,
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
    <form @submit.prevent="handleAddNewVehicle()">
        <OneColFormWrapper class="w-full">
            <InputBox
                title="Số hộ khẩu"
                placeholder="Số hộ khẩu"
                type="number"
                warn="Số hộ khẩu phải là số"
                @update="household_id = $event.value"
            />
            <InputBox
                title="Biển số xe"
                placeholder="Biển số xe"
                @update="license_plate = $event.value"
            />
            <div class="w-full">
                <div class ="mx-auto mb-2 text-start">Loại xe</div>
                <select v-model="vehicle_type" class="select select-bordered w-full">
                    <option disabled selected value ="">Chọn loại xe</option>
                    <option value="1">Xe máy</option>
                    <option value="2">Ô tô</option>
                </select>
            </div>
            <button
                type = "submit"
                class="btn btn-primary w-full">
                Đăng ký
            </button>
        </OneColFormWrapper>
    </form>
</template>