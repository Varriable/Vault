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