<script>
    import DrawerContent from "./DrawerContent.svelte";

    import MainTable from "./MainTable.svelte";

    import { pb } from "$lib/pocketbase.js";
    import { onMount } from "svelte";
    import { PUBLIC_SERVER, PUBLIC_POCKET } from "$env/static/public";

    let charge = "Charge";

    let records = [];
    let loading = false;
    let recImg = "";

    let items = [];
    let data = {
        data: {
            items: [
                {
                    name: "string",
                    price: "string",
                },
            ],
            id: "string",
        },
        created: "string",
    };

    onMount(async () => {
        records = await pb.collection("receipts").getFullList({
            sort: "-created",
            expand: "user",
        });
        console.log(records);
    });

    const setData = (d) => {
        data = d;
        recImg = `${PUBLIC_POCKET}/api/files/receipts/${d.id}/${d.rec}`;
        console.log("The data we are looking for", { data });
        open = true;
    };

    async function handleFileUpload(event) {
        loading = true;
        const file = event.target.files[0];

        console.log("handle upload");

        const formData = new FormData();
        formData.append("file", file);
        formData.append("charge", charge);
        formData.append("token", pb.authStore.model?.id);

        try {
            const response = await fetch(`${PUBLIC_SERVER}/extract_text`, {
                method: "POST",
                body: formData,
                //   headers: {
                //   'Authorization': 'Bearer your_token_here'
                // },
            });

            if (response.ok) {
                console.log("File uploaded successfully!");
            } else {
                console.error("Error uploading file.");
            }
        } catch (error) {
            console.error("An error occurred while uploading the file:", error);
        } finally {
            loading = false;
        }
    }

    import Drawer from 'svelte-drawer-component'
    let open = false
</script>

<div class="flex justify-center items-center gap-5">
    <h1 class="text-4xl font-bold text-center py-10">Receipts</h1>
</div>

{#if loading}
    <div class="w-full text-center justify-center grid pb-10">
        <h1 class="p-2">Loading...</h1>
        <progress class="h-10 progress w-96" />
    </div>
{:else}
    <div class="flex justify-center pb-10">
        <input
            class="border-2 border-primary"
            type="file"
            on:change={handleFileUpload}
        />
        <select
            bind:value={charge}
            class="select select-primary w-full max-w-xs"
        >
            <option disabled selected>Charge</option>
            <option>Personal</option>
            <option>House</option>
        </select>
    </div>
{/if}

<div class="px-10">
    <div class="overflow-x-auto">
        <MainTable {records} {setData} />
    </div>
</div>

<Drawer  on:clickAway={() => open = false} { open } size='90%'>
    <div class="bg-black h-full overflow-y-scroll">
        <div class="flex justify-end p-5 text-2xl">
            <button on:click={() => open = false}>X close</button>
        </div>
        <DrawerContent {recImg} {data} />
    </div>
</Drawer>
