<script>

  import { pb } from '$lib/pocketbase.js'
  import { goto } from '$app/navigation';
  import { onMount } from 'svelte';

  onMount(() => {
    if (pb.authStore.isValid) {
      goto('/app')
    }
  })

  let user = ""
  let pass = ""

  const login = async () => {
    const authData = await pb.collection('users').authWithPassword(
      user,
      pass,
    );

    if(pb.authStore.isValid) {
      goto("/app")
    } else {
      alert("error loggin in")
    }


  // after the above you can also access the auth data from the authStore
  console.log(pb.authStore.isValid);

  }

</script>


<div class="hero min-h-screen bg-base-200">
    <div class="hero-content flex-col lg:flex-row-reverse">
      <div class="text-center lg:text-left">
        <h1 class="text-5xl font-bold">Login</h1>
      </div>
      <div class="card flex-shrink-0 w-full max-w-sm shadow-2xl bg-base-100">
        <div class="card-body">
          <div class="form-control">
            <label class="label">
              <span class="label-text">Username</span>
            </label>
            <input bind:value={user} type="text" placeholder="username" class="input input-bordered" />
          </div>
          <div class="form-control">
            <label class="label">
              <span class="label-text">Password</span>
            </label>
            <input bind:value={pass} type="text" placeholder="password" class="input input-bordered" />
            <label class="label">
            </label>
          </div>
          <div class="form-control mt-6">
            <button on:click={login} class="btn btn-primary">Login</button>
          </div>
        </div>
      </div>
    </div>
  </div>