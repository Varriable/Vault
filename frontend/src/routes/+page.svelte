<script lang="ts">
    import { userStore } from '$lib/index';
    import { login } from '$lib/api/auth';
    let email = $state('')
    let password = $state('')

    function handleLogin() {
        console.log('Attempting login with email:', email);
        login(email, password)
        console.log('User logged in:', userStore.user);
    }
</script>

{#if userStore.user}
    <h1>Welcome, {userStore.user.name}!</h1>
{:else}
    <h1>Please log in to access your vault.</h1>
    <input type="text" placeholder="email" bind:value={email} />
    <input type="password" placeholder="Password" bind:value={password} />
    <button onclick={handleLogin}>Login</button>
{/if}