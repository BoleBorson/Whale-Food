<script>
    import { pb } from "$lib/pocketbase.js";
    import { goto } from '$app/navigation';
    import { notifications } from "$lib/notifications";

    const data = {
        "username": "",
        "email": "",
        "emailVisibility": true,
        "password": "",
        "passwordConfirm": "",
        "name": ""
    };

    const register = async () => {
        console.log(data)
        if(data.password !== data.passwordConfirm) {
            notifications.danger("Passwords do not match...", 1000)
            return
        }

        try {
            await pb.collection('users').create(data);
        } catch (e) {
            notifications.danger('Error creating account...', 1000)
            return
        }

        await pb.collection('users').authWithPassword(
            data.username,
            data.password,
        );

        if(pb.authStore.isValid) {
            notifications.success('Account Created! Loggin in...', 1000)
            goto("/app")
        } else {
            notifications.danger('Error creating account...', 1000)
        }
    }

    const onKeyDown = (e) => {
        if (e.keyCode === 13) {
            register()
        }
	}


</script>

<svelte:window on:keydown={onKeyDown} />

<div class="flex justify-center">
    <div class="hero-content flex-col gap-10 justify-center">
        <div class="text-center lg:text-left">
            <h1 class="text-5xl font-bold">Register</h1>
        </div>
        <div class="card flex-shrink-0 w-full max-w-sm shadow-2xl bg-base-100">
            <div class="card-body">
                <div class="form-control">
                    <label class="label">
                        <span class="label-text">Username</span>
                    </label>
                    <input
                        bind:value={data.username}
                        type="text"
                        placeholder="username"
                        class="input input-bordered"
                    />
                </div>
                <div class="form-control">
                    <label class="label">
                        <span class="label-text">Email</span>
                    </label>
                    <input
                        bind:value={data.email}
                        type="text"
                        placeholder="email"
                        class="input input-bordered"
                    />
                </div>
                <div class="form-control">
                    <label class="label">
                        <span class="label-text">Name</span>
                    </label>
                    <input
                        bind:value={data.name}
                        type="text"
                        placeholder="name"
                        class="input input-bordered"
                    />
                </div>
                <div class="form-control">
                    <label class="label">
                        <span class="label-text">Password</span>
                    </label>
                    <input
                        bind:value={data.password}
                        type="password"
                        placeholder="password"
                        class="input input-bordered"
                    />
                </div>
                <div class="form-control">
                    <label class="label">
                        <span class="label-text">Confirm Password</span>
                    </label>
                    <input
                        bind:value={data.passwordConfirm}
                        type="password"
                        placeholder="password"
                        class="input input-bordered"
                    />
                </div>
                <div class="form-control mt-6">
                    <button on:click={register} class="btn btn-primary">Register</button>
                </div>
            </div>
        </div>
    </div>
</div>

