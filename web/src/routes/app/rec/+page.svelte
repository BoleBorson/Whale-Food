<script lang="ts">
  import { pb } from '$lib/pocketbase.js'
  import { onMount } from 'svelte'
  import { notifications } from '$lib/notifications.js'
  import Toast from '$lib/Toast.svelte'
  import RecImgModel from '$lib/RecImgModel.svelte';
  import { PUBLIC_SERVER, PUBLIC_POCKET } from '$env/static/public';

  interface record {
    expand: {
      user: {
        username: string
      }
    }
    data: {
      store: string,
      total: string,
      type: string
    },
    created: string

  }

  interface item {

  }

  let charge: string = "Charge"

  let records: record[] = []
  let loading = false
  let recImg:string = ""

  let items: item[] = []
  let data = {
      data: {
        items: [{
          name: "string",
          price: "string"
        }],
        id: "string"
      },
      created: "string"
  }

  onMount(async () => {
    records = await pb.collection('receipts').getFullList({
      sort: '-created',
      expand: 'user'
    });
    console.log(records)
  })

  const setData = (d) => {
    data = d
    recImg = `http://${PUBLIC_POCKET}/api/files/receipts/${d.id}/${d.rec}`
    console.log("The data we are looking for", {data})
  }

  const updateRec = async () => {

    let newRec = records.find(obj => obj.id === data.id)
    console.log(newRec)

    let jsonNew = data
    data.items = items
    console.log(jsonNew)
    // example update data
    let update = {
        "data": data.data,
        "charge": newRec.charge
    };

    const record = await pb.collection('receipts').update(data.id, update)
    .finally(() => {
      notifications.success('Edits Saved Succesfully', 2000)
    })
  }

  const deleteRec = async (id: string) => {
    records = records.filter(obj => obj.id !== id)
    await pb.collection('receipts').delete(id);
  }

  async function handleFileUpload(event: { target: { files: any[]; }; }) {
      loading = true;
      const file = event.target.files[0];

      console.log("handle upload");

      const formData = new FormData();
      formData.append('file', file);
      formData.append('charge', charge)
      formData.append('token', pb.authStore.model?.id)

      try {
        const response = await fetch(``http`://${PUBLIC_SERVER}/extract_text`, {
          method: 'POST',
          body: formData,
        //   headers: {
        //   'Authorization': 'Bearer your_token_here'
        // },

        });

        if (response.ok) {
          console.log('File uploaded successfully!');
        } else {
          console.error('Error uploading file.');
        }
      } catch (error) {
        console.error('An error occurred while uploading the file:', error);
      } finally {
        loading = false;
      }
  }

  const formatDate = (ds: string) => {
    let date = new Date(ds);

    // Format the date as Eastern Time
    let options = {
      timeZone: 'America/New_York', 
      year: 'numeric',
      month: 'long',
      day: 'numeric'
    };

    return date.toLocaleString('en-US', options);

  }

</script>



<Toast />
<div class="drawer">
  <input id="my-drawer" type="checkbox" class="drawer-toggle" />
  <div class="drawer-content">
    <div class="flex justify-center items-center gap-5">
      <h1 class="text-4xl font-bold text-center py-10">Receipts</h1>
  
</div>

{#if loading}
  <div class="w-full text-center justify-center grid pb-10">
    <h1 class="p-2">Loading...</h1>
    <progress class="h-10 progress w-96"></progress>
  </div>
{:else}
  <div class="flex justify-center pb-10">
    <input class="border-2 border-primary" type="file" on:change={handleFileUpload} />
    <select bind:value={charge} class="select select-primary w-full max-w-xs">
      <option disabled selected>Charge</option>
      <option>Personal</option>
      <option>House</option>
    </select>
  </div>
{/if}

    <div class="px-10">
      <div class="overflow-x-auto">
        <table class="table w-full">
          <!-- head -->
          <thead>
            <tr>
              <th></th>
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
                    <label on:click={() => setData(r)} for="my-drawer" class="btn btn-primary btn-xs">more</label>
                    <button on:click={() => deleteRec(r.id)} class="btn btn-error btn-xs">delete</button>
                </td>
              </tr>
            {/each}
          </tbody>
        </table>
      </div>
    </div>
    
  </div> 
  <div class="drawer-side">
    <label for="my-drawer" class="drawer-overlay"></label>
    <ul class="menu p-4 w-3/4 bg-base-100 text-base-content">
      <!-- Sidebar content here -->
      <div class="">
        <div class="w-full stats bg-primary text-primary-content mb-5">
  
          <div class="stat">
            <div class="stat-title">Store</div>
            <div class="stat-value">
              <input class="input text-3xl w-56 bg-transparent" type="text" bind:value={data.data.store} name="" id="">
            </div>
          </div>
          
          <div class="stat">
            <div class="stat-title">Total Price</div>
            <div class="stat-value">
              <input class="text-3xl w-40 bg-transparent" type="text" bind:value={data.data.total} name="" id="">
            </div>
          </div>

          <div class="stat">
            <div class="stat-title">Total Price</div>
            <div class="stat-value">
              <input class="text-3xl w-40 bg-transparent" type="text" bind:value={data.charge} name="" id="">
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
                    <th></th>
                    <th>Item</th>
                    <th>Price</th>
                  </tr>
                </thead>
                <tbody>
                  {#each data.data.items as d, i}
                    <tr>
                      <th>{i + 1}</th>
                      <td><input class="input h-5 max-w-xs" type="text" bind:value={d.name} name="" id=""></td>
                      <td><input class="input h-5 max-w-xs" type="text" bind:value={d.price} name="" id=""></td>
                    </tr>  
                  {/each}
                </tbody>
              </table>
            </div>
            <div>
              <img src={recImg} alt="">
            </div>
          </div>
          <button on:click={updateRec} class="btn btn-primary w-full">Save Changes</button>
        </div>
      </div>
    </ul>
  </div>
</div>