<script lang="ts">
    import './auth.css'
    import { userStore, login } from '$lib/index';
    import { goto } from '$app/navigation';
    
    let email = $state('')
    let password = $state('')

    function handleLogin() {
        login(email, password)
        console.log('User logged in:', userStore.user);
        goto('/vault')
        
    }
</script>

{#if userStore.user}
    <h1 class="h1">Welcome, {userStore.user.name}!</h1>
{:else}
    <h1 class="h1">Please log in to access your vault.</h1>
    <input class="input" type="text" placeholder="email" bind:value={email} />
    <input class="input" type="password" placeholder="Password" bind:value={password} />
    <button onclick={handleLogin}>Login</button>
    <p class="p">If you dont have an account, you can login here: <a class="a" href='/register'>Sign Up</a></p>
{/if}