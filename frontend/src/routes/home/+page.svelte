<script lang="ts">
    import '../auth.css'
    import { userStore } from '$lib/index';
    import { goto } from '$app/navigation';

    $effect(() => {
        if (!userStore.user) {
            setTimeout(() => {
                goto('/')
            }, 1000)
        }
    })

</script>


<main>
    <h1 class="h1">Welcome to your vault, {userStore.user?.name}!</h1>
    <p class="p">Here you can securely store your secrets and access them whenever you need.</p>
    <p class="p">Use the navigation menu to access different sections of your vault.</p>
</main>
