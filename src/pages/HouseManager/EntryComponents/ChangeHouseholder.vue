<script setup lang="ts">
import { ref } from "vue";


// NOTE: for demonstration only
type Relationship = {
    cccd: string,
    relationship: string,
    birth_id: number | null,
    alive: boolean,
    death_paper_id: number | null,
    household_id: string,
}

type Household = {
    id: string,
    name: string,
    location: string,
    owner: string,
    size: string,
    house_type: string,
}
const HouseholdType = ref<Household>();
const householdId = ref<string>("");
const householders = ref<Array<Relationship>>([]);
const selectedHouseholders = ref<Array<string>>([]);
const selectedCheckbox = ref(-1);
const message = ref("");
async function getData() {
    // NOTE: for demonstration only
    const response = await fetch(`http://localhost:8000/api/relationships/household/${householdId.value}`);

    try {
        const data = await response.json() as Array<Relationship>;
        householders.value = data;
    } catch (error) {
        console.error(error);
    }
};

function toggleFromList(index: number,householderId: string, eventTarget: EventTarget | null) {
    if (eventTarget === null) {
        return;
    }
    if ((eventTarget as HTMLInputElement).checked) {
        selectedCheckbox.value = index;
        const householder = householders.value.find((h) => h.household_id === householderId);
        if (householder) {
            selectedHouseholders.value.push(householder.household_id);
        }
    } else {
        selectedCheckbox.value = -1;
        selectedHouseholders.value = selectedHouseholders.value.filter((h) => h !== householderId);
    }
}

async function ChangeOwner() {
    const response = await fetch(`http://localhost:8000/api/household_registrations/${householdId.value}`);
    const data = await response.json();
    HouseholdType.value = data;
    
    if (HouseholdType.value) {
        HouseholdType.value.owner = selectedHouseholders.value[0];
    }
    const response2 = await fetch(`http://localhost:8000/api/household_registrations/${householdId.value}`, {
        method: "PUT",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify(HouseholdType.value),
    });

    if (response2.ok) {
        message.value = "Thay đổi chủ hộ thành công";
    } else {
        message.value = response2.statusText;
    }
}
</script>

<template>
    <div class="flex flex-col gap-3">
        <input type="text" placeholder="Nhập số hộ khẩu" class="input input-bordered w-full max-w-xs"
            v-model="householdId" @change="getData" />

        <table>
            <thead class="[&_th]:min-w-[200px] [&_th]:px-4 [&_th]:py-2">
                <tr>
                    <th>Hộ khẩu</th>
                    <th>CCCD</th>
                    <th>Chọn</th>
                </tr>
            </thead>
            <tbody
                class="[&_td]:min-w-[200px] [&_td]:border [&_td]:px-4 [&_td]:py-2"
			>
                <tr
                    v-for="(item, index) in householders"
                    :key="`${item.household_id}-${index}`"
                    >
                    <td>{{ item.household_id }}</td>
                    <td>{{ item.cccd }}</td>
                    <td>
                        <input
                            type="checkbox"
                            :value="item.household_id"
                            :checked="selectedCheckbox === index"
                            @change="toggleFromList(index, item.household_id, $event.target)"
                        />
                    </td>
                </tr>
                </tbody>
        </table>
        <button class="btn btn-primary" @click="ChangeOwner">Đổi chủ hộ</button>
        <div v-if="message">{{ message }}</div>
    </div>
</template>

