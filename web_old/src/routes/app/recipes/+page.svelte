<script>
    import RecipieDrawer from "$lib/RecipieDrawer.svelte";

    import { onMount } from 'svelte';
    import { pb } from '$lib/pocketbase.js'

    // @ts-ignore
    /**
     * @type {any[]}
     */
    let records = []

    onMount(async () => {
        records = await pb.collection('recipes').getFullList({
            sort: '-created',
        })

        console.log(records)
    })

</script>

<div class="flex flex-wrap gap-5 m-5">
    {#each records as r}
        <div class="card w-96 bg-base-100 shadow-xl image-full">
            <figure><img src="https://i2.wp.com/www.downshiftology.com/wp-content/uploads/2021/05/Chicken-Stir-Fry-main-1.jpg" alt="Shoes" /></figure>
            <div class="card-body">
                <h2 class="card-title">{r.title}</h2>
                <p>$ {r.chat.total_price}</p>
                <div class="card-actions justify-end">
                    <a href={`/app/recipes/recipe-${r.id}`} class="btn btn-primary">Full Recipie</a>
                </div>
            </div>
        </div>
    {/each}

    <div class="card w-96 bg-base-100 shadow-xl image-full hover:opacity-90 shadow-2xl cursor-pointer">
        <figure><img src="https://www.freepnglogos.com/uploads/plus-icon/plus-icon-plus-math-icon-download-icons-9.png" alt="Shoes" /></figure>
        <div class="card-body">
            <h2 class="card-title">New</h2>
            <div class="card-actions justify-end">
                <!-- <a  class="btn btn-primary">Full Recipie</a> -->
            </div>
        </div>
    </div>
</div>
