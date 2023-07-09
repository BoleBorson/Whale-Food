<script>
    import { goto } from '$app/navigation'
    import { pb } from '$lib/pocketbase.js'

    const logout = () => {
        pb.authStore.clear()
        goto("/auth")
    }
</script>

<div class="navbar bg-base-100">
    <div class="navbar-start">
        <div class="dropdown">
            <!-- svelte-ignore a11y-no-noninteractive-tabindex -->
            <!-- svelte-ignore a11y-label-has-associated-control -->
            <label tabindex="0" class="btn btn-ghost lg:hidden">
                <svg
                    xmlns="http://www.w3.org/2000/svg"
                    class="h-5 w-5"
                    fill="none"
                    viewBox="0 0 24 24"
                    stroke="currentColor"
                    ><path
                        stroke-linecap="round"
                        stroke-linejoin="round"
                        stroke-width="2"
                        d="M4 6h16M4 12h8m-8 6h16"
                    /></svg
                >
            </label>
            
            <ul
                tabindex="0"
                class="menu menu-sm dropdown-content mt-3 z-[1] p-2 shadow bg-base-100 rounded-box w-52"
            >
                <li><a href="/app/list">Shopping List</a></li>
                <li>
                    <div>Receipts</div>
                    <ul class="p-2">
                        <li><a href="/app/rec">Receipt Data</a></li>
                        <li><a href="/app/rec-a">Receipt Statistics</a></li>
                    </ul>
                </li>
                <!-- <li><a>Item 3</a></li> -->
            </ul>
        </div>
        <a class="btn btn-ghost normal-case text-xl">Whale Food</a>
    </div>
    <div class="navbar-center hidden lg:flex">
        <ul class="menu menu-horizontal px-1">
            <li><a href="/app/list">Shopping List</a></li>
            <li tabindex="0">
                <details>
                    <summary>Reciepts</summary>
                    <ul class="p-2">
                        <li><a href="/app/rec">Receipt Data</a></li>
                        <li><a href="/app/rec-a">Receipt Statistics</a></li>
                    </ul>
                </details>
            </li>
            <!-- <li><a>Item 3</a></li> -->
        </ul>
    </div>
    <div class="navbar-end">
        <button on:click={logout} class="btn">Logout</button>
    </div>
</div>

<slot />
