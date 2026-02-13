<script lang="ts">
    import { user } from '$lib/store/userStore';
    import { login } from '$lib/api/auth';
	import { enableCompileCache } from 'module';
    let email = $state('')
    let password = $state('')

    function handleLogin() {
        login(email, password)
    }
</script>

{#if user}
    <h1>Welcome, {user.name}!</h1>
{:else}
    <h1>Please log in to access your vault.</h1>
    <input type="text" placeholder="email" bind:value={email} />
    <input type="password" placeholder="Password" bind:value={password} />
    <button onclick={handleLogin}>Login</button>
{/if}