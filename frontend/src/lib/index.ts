// place files you want to import through the `$lib` alias in this folder.
import {apiRequest} from './api/client';
import { userStore } from './store/userStore.svelte';
import { login, register, logout } from './api/auth';


//types
type User = {
    id: number;
    email: string;
    name: string;
}

type Secret = {
    id: number;
    title: string;
    key: string;
    created_at: string;
    updated_at: string;
}



export {
    apiRequest,
    userStore,
    type User,
    type Secret,
    login,
    register,
    logout,
}