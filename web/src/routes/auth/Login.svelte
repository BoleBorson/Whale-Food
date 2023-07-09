<script>
    import { pb } from "$lib/pocketbase.js";
    import { goto } from '$app/navigation';
    import { notifications } from "$lib/notifications";
    let user = ""
    let pass = ""

    const login = async () => {
        try {
            await pb.collection('users').authWithPassword(
                user,
                pass,
            );
        } catch (e) {
            notifications.danger('Error Logging in...', 1000)
            return
        }

        if(pb.authStore.isValid) {
            notifications.success('Logged In!', 1000)
            goto("/app")
        } else {
            notifications.danger('Incorrect Login...', 1000)
        }
    }   

    const onKeyDown = (e) => {
        if (e.keyCode === 13) {
            login()
        }
	}


</script>

<svelte:window on:keydown={onKeyDown} />

    <div class="flex justify-center">
        <div class="hero-content flex-col gap-10 justify-center">
            <div class="text-center lg:text-left">
                <h1 class="text-5xl font-bold">Login</h1>
            </div>
            <div class="card flex-shrink-0 w-full max-w-sm shadow-2xl bg-base-100">
                <div class="card-body">
                    <div class="form-control">
                        <label class="label">
                            <span class="label-text">Username</span>
                        </label>
                        <input
                            bind:value={user}
                            type="text"
                            placeholder="username"
                            class="input input-bordered"
                        />
                    </div>
                    <div class="form-control">
                        <label class="label">
                            <span class="label-text">Password</span>
                        </label>
                        <input
                            bind:value={pass}
                            type="password"
                            placeholder="password"
                            class="input input-bordered"
                        />
                    </div>
                    <div class="form-control mt-6">
                        <button on:click={login} class="btn btn-primary">Login</button>
                    </div>
                </div>
            </div>
        </div>
    </div>

