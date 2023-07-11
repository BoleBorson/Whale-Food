<script>
    import MainTable from "./MainTable.svelte";

    import { pb } from "$lib/pocketbase.js";
    import { onMount } from "svelte";
    import { notifications } from "$lib/notifications.js";
    import RecImgModel from "$lib/RecImgModal.svelte";
    import { PUBLIC_SERVER, PUBLIC_POCKET } from "$env/static/public";

    export let data;
    export let recImg;
    let charge = "Charge";

    let records = [];
    let loading = false;

    let items = [];

    const updateRec = async () => {
        let newRec = records.find((obj) => obj.id === data.id);
        console.log(newRec);

        let jsonNew = data;
        data.items = items;
        console.log(jsonNew);
        // example update data
        let update = {
            data: data.data,
            charge: data.charge,
        };

        const record = await pb
            .collection("receipts")
            .update(data.id, update)
            .finally(() => {
                notifications.success("Edits Saved Succesfully", 2000);
            });
    };

    const formatDate = (ds) => {
        let date = new Date(ds);

        // Format the date as Eastern Time
        let options = {
            timeZone: "America/New_York",
            year: "numeric",
            month: "long",
            day: "numeric",
        };

        return date.toLocaleString("en-US", options);
    };
</script>

<div class="p-5">
    <div class="w-full stats bg-primary text-primary-content mb-5">
        <div class="stat">
            <div class="stat-title">Store</div>
            <div class="stat-value">
                <input
                    class="input text-3xl w-56 bg-transparent"
                    type="text"
                    bind:value={data.data.store}
                    name=""
                    id=""
                />
            </div>
        </div>

        <div class="stat">
            <div class="stat-title">Total Price</div>
            <div class="stat-value">
                <input
                    class="text-3xl w-40 bg-transparent"
                    type="text"
                    bind:value={data.data.total}
                    name=""
                    id=""
                />
            </div>
        </div>

        <div class="stat">
            <div class="stat-title">Total Price</div>
            <div class="stat-value">
                <input
                    class="text-3xl w-40 bg-transparent"
                    type="text"
                    bind:value={data.charge}
                    name=""
                    id=""
                />
            </div>
        </div>

        <div class="stat">
            <div class="stat-title">Date</div>
            <div class="stat-value">{formatDate(data.created)}</div>
        </div>
    </div>
    <div class="overflow-x-auto">
        <div class="flex">
            <div>
                <table class="table w-full">
                    <!-- head -->
                    <thead>
                        <tr>
                            <th />
                            <th>Item</th>
                            <th>Price</th>
                        </tr>
                    </thead>
                    <tbody>
                        {#each data.data.items as d, i}
                            <tr>
                                <th>{i + 1}</th>
                                <td
                                    ><input
                                        class="input h-5 max-w-xs"
                                        type="text"
                                        bind:value={d.name}
                                        name=""
                                        id=""
                                    /></td
                                >
                                <td
                                    ><input
                                        class="input h-5 max-w-xs"
                                        type="text"
                                        bind:value={d.price}
                                        name=""
                                        id=""
                                    /></td
                                >
                            </tr>
                        {/each}
                    </tbody>
                </table>
            </div>
            <div>
                <img src={recImg} alt="" />
            </div>
        </div>
        <div class="flex justify-center p-5">
            <button on:click={updateRec} class="btn btn-success w-full ">Save Changes</button>
        </div>
    </div>
</div>
