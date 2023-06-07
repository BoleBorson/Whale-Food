

<script>

import { onMount } from 'svelte';
import { createEventDispatcher } from 'svelte';

  const items = [
    {
      "id": 1,
      "name": "Pasta Sauce",
      "progress": {
        "value": 100,
        "max": 100,
        "class": "progress-success w-56"
      },
      "expiration_date": "06/06/2023",
      "category": "Sauce"
    },
    {
      "id": 2,
      "name": "Bread",
      "progress": {
        "value": 15 ,
        "max": 100,
        "class": "progress-warning w-56"
      },
      "expiration_date": "08/15/2022",
      "category": "Bakery"
    },
    {
      "id": 3,
      "name": "Milk",
      "progress": {
        "value": 60,
        "max": 100,
        "class": "progress-info w-56"
      },
      "expiration_date": "07/01/2022",
      "category": "Dairy"
    },
    {
      "id": 4,
      "name": "Eggs",
      "progress": {
        "value": 25,
        "max": 100,
        "class": "progress-danger w-56"
      },
      "expiration_date": "06/20/2022",
      "category": "Dairy"
    },
    {
      "id": 5,
      "name": "Apples",
      "progress": {
        "value": 90,
        "max": 100,
        "class": "progress-success w-56"
      },
      "expiration_date": "06/30/2022",
      "category": "Fruit"
    }
  ];

  function getProgressClass(value) {
    if (value >= 75) {
      return "progress-success w-56";
    } else if (value >= 50) {
      return "progress-warning w-56";
    } else if (value >= 25) {
      return "progress-error w-56";
    } else {
      return "progress-danger w-56";
    }
  }

  const dispatch = createEventDispatcher();

  let searchTerm = '';

  function handleSearch(event) {
    searchTerm = event.target.value;
    dispatch('search', searchTerm);
  }

  onMount(() => {
    dispatch('search', searchTerm);
  });

</script>

<body class="flex justify-center">

<div class="flex flex-col items-center">

    <h1 class="text-2xl font-bold">Inventory</h1>

<div class="p-4">
    <div class="flex items-center justify-between mb-4">
      
      <div class="relative">
        <input type="text" class="input input-bordered" placeholder="Search" on:input={handleSearch} bind:value={searchTerm} />
      </div>
    </div>
</div>

<div class="overflow-x-auto">
    <table class="table table-zebra">
        <!-- head -->
        <thead>
          <tr>
            <th></th>
            <th>Item Name</th>
            <th>Quantity</th>
            <th>Purchase Date</th>
            <th>Category</th>
          </tr>
        </thead>
        <tbody>
          {#each items.filter(item => item.name.toLowerCase().includes(searchTerm.toLowerCase())) as item}
            <tr>
              <th>{item.id}</th>
              <td>{item.name}</td>
              <td>
                <div class="progress-container">
                  <progress class={"progress " + getProgressClass(item.progress.value)} value={item.progress.value} max={item.progress.max}></progress>
                  <span class="progress-text">{item.progress.value}%</span>
                </div>
              </td>
              <td>{item.expiration_date}</td>
              <td>{item.category}</td>
            </tr>
          {/each}
        </tbody>
      </table>
</div>
</div>

</body>