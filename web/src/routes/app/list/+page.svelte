<script lang="ts">
    import { pb } from '$lib/pocketbase.js'
    import { onMount } from 'svelte'

    let records = []

    onMount(async () => {
        records = await pb.collection('list').getFullList({
            sort: '-created',
        });
    })

    const add = async () => {
        let item = {
            "item": "",
            "price": "",
            "checked": false
        }
        records = [item, ...records]

        await pb.collection('list').create(item);
    }

    const remove = async () => {
        let checked = records.filter(r => r.checked)
        console.log(checked)

        records = records.filter(r => !r.checked)

        checked.forEach(async (r) => {
            await pb.collection('list').delete(r.id);
        })
    }

    const updateCheck = async (id) => {
        let record = records.find(r => r.id == id)
        record.checked = !record.checked

        await pb.collection('list').update(record.id, record);
    }

    const updateItem = async (record) => {
        await pb.collection('list').update(record.id, record);
    }

</script>

<h1 class="text-3xl font-bold text-center p-10">Shopping List</h1>

<div class="flex justify-center gap-5 pb-5">
    <div>
        <button on:click={add} class="btn btn-success">add item</button>
    </div>
    <div>
        <button on:click={remove} class="btn btn-error">remove checked</button>
    </div>
</div>

<div class="flex justify-center">
    <div class="justify-center">
        <div class="overflow-x-auto m-2 max-w-2xl">
            <table class="table w-full ">
                <!-- head -->
                <thead>
                    <tr>
                    <th>
                        <label>
                            <input type="checkbox" class="checkbox" />
                        </label>
                    </th>
                    <th>Item</th>
                    <th>Price</th>
                    </tr>
                </thead>
                <tbody>
                    <!-- row 1 -->
                   {#each records as r}
                   <tr>
                        <th>
                            <label>
                                <input bind:checked={r.checked} on:click={() => updateCheck(r.id)} type="checkbox" class="checkbox" />
                            </label>
                        </th>
                        <td>
                            <input placeholder="new item" class=" w-[190px] appearance-none bg-transparent border-none outline-none p-0 m-0" on:blur={() => updateItem(r)} bind:value={r.item} type="text"/>
                        </td>
                        <td>
                            <input placeholder="price class=" class="w-[40px] appearance-none bg-transparent border-none outline-none p-0 m-0" on:blur={() => updateItem(r)} bind:value={r.price} type="text"/>
                        </td>
                    </tr>
                   {/each}
                </tbody>
            </table>
        </div>
    </div>
</div>