<script>
  import { onMount } from "svelte";
  import { pb } from "$lib/pocketbase.js";


  let records = [];

  let coleSum = 0;
  let shelleySum = 0;
  let joeSum = 0;

  let coleHouse = 0;
  let shelleyHouse = 0;
  let joeHouse = 0;



  onMount(async () => {
    records = await pb.collection('receipts').getFullList({
        sort: '-created',
        expand: 'user'
    });

    console.log(records);

    let house = records.filter(record => record.charge === 'House');
    console.log(house);

    let joeHouseRecords = house.filter(record => record.expand.user.username === 'joe');
    // now shelley
    let shelleyHouseRecords = house.filter(record => record.expand.user.username === 'shelley');
    //now cole
    let coleHouseRecords = house.filter(record => record.expand.user.username === 'cole');


    joeHouse = joeHouseRecords.reduce((sum, obj) => sum + parseInt(obj.data.total), 0);
    shelleyHouse = shelleyHouseRecords.reduce((sum, obj) => sum + parseInt(obj.data.total), 0);
    coleHouse = coleHouseRecords.reduce((sum, obj) => sum + parseInt(obj.data.total), 0);


    

    // pull out all records where user username = 'joe'
    // with map function
    let joeRecords = records.filter(record => record.expand.user.username === 'joe');
    console.log(joeRecords);
    // now shelley
    let shelleyRecords = records.filter(record => record.expand.user.username === 'shelley');
    //now cole
    let coleRecords = records.filter(record => record.expand.user.username === 'cole');


    joeSum = joeRecords.reduce((sum, obj) => sum + parseInt(obj.data.total), 0);
    console.log(joeSum);
    shelleySum = shelleyRecords.reduce((sum, obj) => sum + parseInt(obj.data.total), 0);
    console.log(shelleySum);
    coleSum = coleRecords.reduce((sum, obj) => sum + parseInt(obj.data.total), 0);
    console.log(coleSum);
  });



</script>
  
  <!-- <Bar {data} options={{ responsive: true }} /> -->

  <!-- header -->
  <h1 class="text-center text-3xl font-bold p-10">Whales Stingy Stats</h1>

  <h1 class="text-2xl pl-20 font-bold">House</h1>  
  <div class="flex justify-center m-10 stats bg-primary text-primary-content">
  
    <div class="stat">
      <div class="stat-title">Nemo</div>
      <div class="stat-value">${joeHouse}</div>
    </div>

    <div class="stat">
      <div class="stat-title">Kitty</div>
      <div class="stat-value">${coleHouse}</div>
    </div>

    <div class="stat">
      <div class="stat-title">Darth</div>
      <div class="stat-value">${shelleyHouse}</div>
    </div>
    
  </div>  

  <h1 class="text-2xl pl-20 font-bold">Total</h1>

  <div class="flex justify-center m-10 stats bg-primary text-primary-content">
  
    <div class="stat">
      <div class="stat-title">Nemo</div>
      <div class="stat-value">${joeSum}</div>
    </div>

    <div class="stat">
      <div class="stat-title">Kitty</div>
      <div class="stat-value">${coleSum}</div>
    </div>

    <div class="stat">
      <div class="stat-title">Darth</div>
      <div class="stat-value">${shelleySum}</div>
    </div>
    
  </div>    