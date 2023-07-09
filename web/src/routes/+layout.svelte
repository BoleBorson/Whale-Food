<script>
    import "../app.css";
    import { goto } from '$app/navigation';
    import { onMount } from 'svelte';
    import { pb } from '$lib/pocketbase.js';
    import Toast from "$lib/Toast.svelte";

    


    onMount(() => {
        if (pb.authStore.isValid) {
            // goto('/app')
        } else {
            goto('/auth')
        }
    })
</script>
  
<slot />

<Toast />
