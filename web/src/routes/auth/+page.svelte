<script>
    import Login from './Login.svelte';

    import Register from './Register.svelte';

    import { pb } from "$lib/pocketbase.js";
    import { goto } from '$app/navigation';
    import { onMount } from 'svelte';
    // import info from '$lib/info.js';

    onMount(() => {
        if (pb.authStore.isValid) {
            goto('/app')
        }
    })

    let tab = 0

    const setTab = (i) => {
        tab = i
    }


</script>

<h1 class="text-6xl font-bold text-center pt-10">Whale Food</h1>


<div class="flex justify-center">
    <div class="w-72">
        <div class="tabs tabs-boxed max-w-50 justify-center m-10">
            <button on:click={() => setTab(0)} class="tab w-20 {tab === 0 ? 'tab-active' : ''}">Login</button> 
            <button on:click={() => setTab(1)} class="tab {tab === 1 ? 'tab-active' : ''}">New Account</button> 
        </div>
    </div>
</div>
    
    
        
    
{#if tab === 0}
    <Login></Login>
{:else}
    <Register></Register>
{/if}
