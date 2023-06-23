<script>
    /** @type {import('./$types').PageData} */
    export let data;

    import { onMount } from 'svelte';
    import { pb } from '$lib/pocketbase.js'

    let record = {
        chat: {
            shopping: [],
            ingredients: [],
            steps: []
        }
    }

    onMount(async () => {
        record = await pb.collection('recipes').getOne(data.slug, {
            expand: 'relField1,relField2.subRelField',
        });

        console.log(record.chat.shopping)
    })

</script>

<h1 class="text-center text-4xl font-bold pb-10">{record.title}</h1>

<div class="grid justify-center">
    <div class="flex justify-center gap-5 flex-wrap ">
        
        <div>
            <h1 class="text-center p-5 font-bold text-2xl">Shopping</h1>
            <div class="overflow-x-auto">
                <table class="table">
                  <!-- head -->
                  <thead>
                    <tr>
                      <th></th>
                      <th>Name</th>
                      <th>Price</th>
                    </tr>
                  </thead>
                  <tbody>
                    <!-- row 1 -->
                    {#each record.chat.shopping as s, i}
                    <tr>
                        <th>{i + 1}</th>
                        <td>{s.item}</td>
                        <td>${s.price}</td>
                      </tr>
                    {/each}
                  </tbody>
                </table>
              </div>
        </div>
        <div>
            <h1 class="text-center p-5 font-bold text-2xl">Ingredients</h1>
            <div class="overflow-x-auto">
                <table class="table">
                  <!-- head -->
                  <thead>
                    <tr>
                      <th></th>
                      <th>Name</th>
                      <th>Portion</th>
                    </tr>
                  </thead>
                  <tbody>
                    {#each record.chat.ingredients as r, i}
                        <tr>
                            <th>{i + 1}</th>
                            <td>{r.item}</td>
                            <td>{r.portion}</td>
                        </tr>
                    {/each}
                  </tbody>
                </table>
              </div>

        </div>
    </div>
    <div class="grid justify-center">

        <h1 class="text-center p-5 font-bold text-2xl">Steps</h1>
        <div class="overflow-x-auto">
            <table class="table w-10">
                <!-- head -->
                <thead>
                <tr>
                    <th></th>
                    <th>Name</th>
                    <th>Description</th>
                </tr>
                </thead>
                <tbody>
                <!-- row 1 -->
                {#each record.chat.steps as s, i}
                    <tr>
                        <th>{i + 1}</th>
                        <td>{s.title}</td>
                        <td>
                            <div class="w-96 whitespace-normal break-words">{s.description}</div>
                        </td>
                    </tr>
                {/each}
                </tbody>
            </table>
        </div>
    </div>
</div>