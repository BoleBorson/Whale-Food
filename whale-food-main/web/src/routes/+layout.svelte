<script>
    import "../app.css";
    import { pb } from '$lib/pocketbase.js'
    import { goto } from '$app/navigation';
    import { onMount } from 'svelte';

    // onMount(() => {
    //     if (!pb.authStore.isValid) {
    //         goto("/login")
    //     }
    // })

 </script>
  
<slot />