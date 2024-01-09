<script setup lang="ts">
import { ref } from "vue";


// NOTE: for demonstration only
type Householder = {
    id: string,
    name: string,
}

const householdId = ref<string>("");
const householders = ref<Array<Householder>>([]);
const selectedHouseholders = ref<Array<string>>([]);

void (async () => {

    // NOTE: for demonstration only
    const response = await fetch("http://example.com/householders");

    try {
        const data = await response.json() as Array<Householder>;
        householders.value = data;
    } catch (error) {
        console.error(error);
    }
})();

function toggleFromList(householderId: string, eventTarget: EventTarget | null) {
    if (eventTarget === null) {
        return;
    }
    if ((eventTarget as HTMLInputElement).checked) {
        const householder = householders.value.find((h) => h.id === householderId);
        if (householder) {
            selectedHouseholders.value.push(householder.id);
        }
    } else {
        selectedHouseholders.value = selectedHouseholders.value.filter((h) => h !== householderId);
    }
}

async function someHandlerFunction() {

    // NOTE: for demonstration only
    const response = await fetch("http://example.com/householders", {
        method: "POST",
        body: JSON.stringify({
            householdId: householdId.value,
            householderId: selectedHouseholders.value,
        }),
    });

    try {
        const data = await response.json();
        console.log(data);
    } catch (error) {
        console.error(error);
    }
}
</script>

<template>
    <div class="flex flex-col gap-3">
        <input type="text" placeholder="Nhập số hộ khẩu" class="input input-bordered w-full max-w-xs"
            v-model="householdId" />

        <div class="form-control">
            <label class="label" v-for="householder in householders" :key="householder.id">
                <span class="label-text">{{ householder.name }} | {{ householder.id }}</span>
                <input type="checkbox" class="checkbox" @change="toggleFromList(householder.id, $event.target)" />
            </label>
        </div>

        <button class="btn btn-primary" @click="someHandlerFunction">Ví dụ</button>
    </div>
</template>

// TODO: Create a search componet for the household id // TODO: Prints out the
household id and the current householder // TODO: Print out all the members of
the household, with a blue button to change the householder // TODO: Call the
API to change the householder
