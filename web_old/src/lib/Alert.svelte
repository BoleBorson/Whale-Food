<script>
    import { afterUpdate } from 'svelte';
    import { fade } from 'svelte/transition';
  
    export let message;
    let duration = 3000; // Default duration in milliseconds
  
    let isVisible = true;
  
    setTimeout(() => {
      isVisible = false;
    }, duration);
  
    let container;
    let transitionOptions = {
      duration: 500,
      delay: 0,
      easing: cubicOut,
      fallback: null
    };
  
    afterUpdate(() => {
      if (container) {
        transitionOptions.delay = duration;
      }
    });
  </script>
  
  {#if isVisible}
    <div transition:fade={transitionOptions} bind:this={container} class="fixed bottom-0 left-0 w-full">
      <div class="bg-gray-900 text-white text-center py-2">
        <span>{message}</span>
      </div>
    </div>
  {/if}