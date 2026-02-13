<script lang="ts">
    import { userStore, register } from '$lib/index';
    import { goto } from '$app/navigation';

    let email = $state('')
    let name = $state('')
    let password = $state('')
    let confirmPassword = $state('')

    function handleRegister() {
        if (password !== confirmPassword) {
            alert("Passwords do not match!");
            return;
        }
        register(name, email, password)
        console.log('User Regitered:', userStore.user);
        goto('/')        
    }

</script>

<h1>Register</h1>
<input type="text" placeholder="Name" bind:value={name} />
<input type="text" placeholder="email" bind:value={email} />
<input type="password" placeholder="Password" bind:value={password} />
<input type="password" placeholder="Confirm Password" bind:value={confirmPassword} />
<button onclick={handleRegister}>Register</button>
<p>If you already have an account, you can login here: <a href='/'>Login</a></p>