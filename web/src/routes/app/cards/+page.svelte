<script>
    import { pb } from '$lib/pocketbase.js';
    import { onMount } from 'svelte';
    import { PUBLIC_POCKET } from '$env/static/public';
    
    

    let records = [];

    onMount(async () => {
        records = await pb.collection('cards').getFullList({
            sort: '-created',
        });

    })

    let card = {}
    let img = ""
    const setCard = (c) => {
        img = `${PUBLIC_POCKET}/api/files/cards/${c.id}/${c.bar}`
        card = c
    }

</script>

<h1 class="text-3xl font-bold text-center p-10">Store Cards</h1>

<!-- Open the modal using ID.showModal() method -->
<dialog id="my_modal_2" class="modal">
  <form method="dialog" class="modal-box">
    <img src={img} alt="">
  </form>
  <form method="dialog" class="modal-backdrop">
    <button>close</button>
  </form>
</dialog>

<div class="flex justify-center">
    <div class="flex wrap justify-center gap-5 p-5 w-96">
        {#each records as c}
            <ul on:click={() => setCard(c)} onclick="my_modal_2.showModal()" class="menu bg-base-200 w-56 rounded-box gap-5">
                <li class="p-5 font-bold text-center hover:opacity-50 transition-opacity cursor-pointer">{c.name}</li>
            </ul>
        {/each}
    </div>
</div>