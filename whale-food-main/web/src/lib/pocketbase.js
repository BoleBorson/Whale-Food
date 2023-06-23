import PocketBase from 'pocketbase';
import { writable } from 'svelte/store';
import { PUBLIC_POCKET } from '$env/static/public';

export const pb = new PocketBase(`http://${PUBLIC_POCKET}`); 

export const currentUser = writable(pb.authStore.model);

pb.authStore.onChange((auth) => {
    console.log('authStore changed', auth);
    currentUser.set(pb.authStore.model);
});