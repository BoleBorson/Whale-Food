<script>
    import { pb } from "$lib/pocketbase.js";
    import { onMount } from "svelte";
    import RecImgModel from "$lib/RecImgModal.svelte";
    import { notifications } from "$lib/notifications.js";

    export let setData;

    export let records;

    const deleteRec = async (id) => {
        records = records.filter((obj) => obj.id !== id);
        await pb.collection("receipts").delete(id)
        .then(() => {
            notifications.success("Receipt deleted", 1000)
        })
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

<table class="table w-full">
    <!-- head -->
    <thead>
        <tr>
            <th />
            <th>User</th>
            <th>Store</th>
            <th>Total</th>
            <th>Type</th>
            <th>Charge</th>
            <th>Date</th>
            <th>Actions</th>
        </tr>
    </thead>
    <tbody>
        {#each records as r, i}
            <tr>
                <th>{i + 1}</th>
                <td>{r.expand.user.username}</td>
                <td>{r.data.store}</td>
                <td>{r.data.total}</td>
                <td>{r.data.type}</td>
                <td>{r.charge}</td>
                <td>{formatDate(r.created)}</td>
                <td>
                    <RecImgModel img={r.rec} id={r.id} />
                    <!-- svelte-ignore a11y-click-events-have-key-events -->
                    <label
                        on:click={() => setData(r)}
                        for="my-drawer"
                        class="btn btn-primary btn-xs">more</label
                    >
                    <button
                        on:click={() => deleteRec(r.id)}
                        class="btn btn-error btn-xs">delete</button
                    >
                </td>
            </tr>
        {/each}
    </tbody>
</table>
