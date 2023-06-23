<script lang="ts">
  import { goto } from '$app/navigation';
  import { onMount } from 'svelte';

  let isMobile = false;

  const handleResize = () => {
    isMobile = window.innerWidth < 640; // Define your desired breakpoint here
  };

  onMount(() => {
    handleResize();
    window.addEventListener('resize', handleResize);
    return () => {
      window.removeEventListener('resize', handleResize);
    };
  });

  let activeTab = 'app';

  const setActiveTab = (tab:string) => {
    goto(`/${tab}`);
    activeTab = tab;
  };

</script>

<!-- <div class="{isMobile ? 'block' : 'hidden'}">
  <div class="btm-nav">
    <button on:click={() => setActiveTab("app")} class="{activeTab === 'app' ? 'active ': ''} bg-neutral text-pink-600">
      <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 12l2-2m0 0l7-7 7 7M5 10v10a1 1 0 001 1h3m10-11l2 2m-2-2v10a1 1 0 01-1 1h-3m-6 0a1 1 0 001-1v-4a1 1 0 011-1h2a1 1 0 011 1v4a1 1 0 001 1m-6 0h6" /></svg>
      <span class="btm-nav-label">Home</span>
    </button>
    <button on:click={() => setActiveTab("app/rec")} class="{activeTab === 'app/rec' ? 'active ': ''} text-neutral-content">
      <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" /></svg>
      <span class="btm-nav-label">Reciepts</span>
    </button>
    <button on:click={() => setActiveTab("app/recipes")} class="{activeTab === 'app/recipes' ? 'active ': ''} text-teal-600">
      <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z" /></svg>
      <span class="btm-nav-label">Recipies</span>
    </button>
  </div>
</div> -->

<!-- <div class="{isMobile ? 'hidden' : 'block'}"> -->
  <div class="navbar bg-base-100">
    <div class="navbar-start">
      <div class="dropdown">
        <label tabindex="0" class="btn btn-ghost lg:hidden">
          <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h8m-8 6h16" /></svg>
        </label>
        <ul tabindex="0" class="menu menu-sm dropdown-content mt-3 p-2 shadow bg-base-100 rounded-box w-52">
          <li><a href="/app/rec">Receipts</a></li>
          <li><a href="/app/rec-analytics">Receipt Analytics</a></li>
          <li><a href="/app/recipes">Recipies</a></li>
          <li><a href="/app/list">Shopping List</a></li>
        </ul>
      </div>
      <a class="btn btn-ghost normal-case text-xl">WhaleFood</a>
    </div>
    <div class="navbar-center hidden lg:flex">
      <ul class="menu menu-horizontal px-1">
        <li><a href="/app/rec">Receipts</a></li>
        <li><a href="/app/rec-analytics">Receipt Analytics</a></li>
        <li><a href="/app/recipes">Recipies</a></li>
        <li><a href="/app/list">Shopping List</a></li>
      </ul>
    </div>
    <div class="navbar-end">
      <!-- <a class="btn">Button</a> -->
    </div>
  </div>
<!-- </div> -->

<slot/>