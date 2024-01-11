<script setup lang="ts">
import { ref, onMounted } from 'vue';

type Householder = {
    cccd: string,
    relationship: string,
    birth_id: number | null,
    alive: boolean,
    death_paper_id: number | null,
    household_id: string,
}

const householders = ref<Householder[]>([])
const householdId = ref<string>('')
const message = ref<string>('')
const selectedHouseholdersCccd = ref<string[]>([])

async function getData() {
    const response = await fetch(`http://localhost:8000/api/relationships/household/${householdId.value}`);

    try {
        const data = await response.json() as Array<Householder>;
        householders.value = data;
    } catch (error) {
        console.error(error);
    }
};

const toggleFromList = (householderCccd: string, target: EventTarget | null) => {
    if (!target) return

    if ((target as HTMLInputElement).checked) {
        selectedHouseholdersCccd.value.push(householderCccd)
    } else {
        selectedHouseholdersCccd.value = selectedHouseholdersCccd.value.filter((item) => item !== householderCccd)
    }
}

async function createNewHousehold(): Promise<void> {
    const household_id = prompt('Nhập số hộ khẩu mới')
    const name = prompt('Nhập tên hộ khẩu mới')
    const location = prompt('Nhập địa chỉ hộ khẩu mới')
    const creation_date = prompt('Nhập ngày thành lập hộ khẩu mới')
    const owner = prompt('Nhập chủ hộ mới')
    const size = prompt('Nhập số thành viên trong hộ khẩu mới')
    const house_type = prompt('Nhập loại hộ khẩu mới')

    if ([household_id, name, location, creation_date, owner, size, house_type].some((item) => item === null)) {
        return Promise.reject('Tạo hộ khẩu mới thất bại: Bạn đã hủy bỏ')
    }

    const createHouseholdResp = await fetch('http://localhost:8000/api/household', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            accept: 'application/json',
        },
        body: JSON.stringify({
            id: household_id,
            name,
            location,
            creation_date,
            owner,
            size,
            house_type,
        }),
    });
    if (!createHouseholdResp.ok) {
        return Promise.reject(`Tạo hộ khẩu mới thất bại: ${createHouseholdResp.statusText}`)
    }
    const addOwnerResp = await fetch(`http://localhost:8000/api/relationships/${owner}`,
        {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json',
                accept: 'application/json',
            },
            body: JSON.stringify({
                cccd: owner,
                relationship: 'Chủ hộ',
                birth_id: null,
                alive: true,
                death_paper_id: null,
                household_id: household_id,
            }),
        })
    if (!addOwnerResp.ok) {
        return Promise.reject(`Thêm chủ hộ mới thất bại: ${addOwnerResp.statusText}`)
    }
    let failedCccd: Array<string> = []
    await Promise.all(selectedHouseholdersCccd.value.map(async (cccd) => {
        const response = await fetch(`http://localhost:8000/api/relationships/${cccd}`, {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json',
                accept: 'application/json',
            },
            body: JSON.stringify({
                cccd: cccd,
                relationship: 'Thành viên',
                birth_id: null,
                alive: true,
                death_paper_id: null,
                household_id: household_id,
            }),
        })
        if (!response.ok) {
            failedCccd.push(cccd)
        }
        else (message.value = 'Tách hộ khẩu thành công')
    }))
    if (failedCccd.length > 0) {
        return Promise.reject(`Tách hộ khẩu thất bại với các CCCD: ${failedCccd.join(', ')}`)
    }
}

async function addToExistingHousehold(): Promise<void> {
    const household_id = prompt('Nhập số hộ khẩu mới')

    if (!household_id) {
        Promise.reject('Tạo hộ khẩu mới thất bại: Bạn đã hủy bỏ')
    }

    let failedCccd: Array<string> = []
    await Promise.all(selectedHouseholdersCccd.value.map(async (cccd) => {
        const response = await fetch(`http://localhost:8000/api/relationships/${cccd}`, {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json',
                accept: 'application/json',
            },
            body: JSON.stringify({
                cccd: cccd,
                relationship: 'Thành viên',
                birth_id: null,
                alive: true,
                death_paper_id: null,
                household_id: household_id,
            }),
        })
        if (!response.ok) {
            failedCccd.push(cccd)
        }
        if (failedCccd.length > 0) {
            return Promise.reject(`Tách hộ khẩu thất bại với các CCCD: ${failedCccd.join(', ')}`)
        }
    }))
}

async function splitHouseholder() {
    if (confirm(`Bạn có muốn tạo hộ khẩu mới cho ${selectedHouseholdersCccd.value.length} người này?`)) {
        try {
            await createNewHousehold()
        } catch (error) {
            message.value = error as string;
        }
        return;
    }

    try {
        await addToExistingHousehold()
    } catch (error) {
        message.value = error as string;
    }
}

onMounted(() => {
    getData()
})
</script>

<template>
    <div class="flex flex-col gap-3">
        <input type="text" placeholder="Nhập số hộ khẩu" class="input input-bordered w-full max-w-xs" v-model="householdId"
            @change="getData" />

        <table>
            <thead class="[&_th]:min-w-[200px] [&_th]:px-4 [&_th]:py-2">
                <tr>
                    <th>Hộ khẩu</th>
                    <th>CCCD</th>
                    <th>Chọn</th>
                </tr>
            </thead>
            <tbody class="[&_td]:min-w-[200px] [&_td]:border [&_td]:px-4 [&_td]:py-2">
                <tr v-for="(item, index) in householders" :key="`${item.household_id}-${index}`">
                    <td>{{ item.household_id }}</td>
                    <td>{{ item.cccd }}</td>
                    <td>
                        <input type="checkbox" :value="item.household_id"
                            @change="toggleFromList(item.cccd, $event.target)" />
                    </td>
                </tr>
            </tbody>
        </table>
        <button class="btn btn-primary w-80 self-center" @click="splitHouseholder">Tách chủ hộ</button>
        <div v-if="message">{{ message }}</div>
    </div>
</template>
