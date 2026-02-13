import { type User } from '$lib/index';
import { browser } from '$app/environment';

let user: User | null = null;

if (browser) {
    const storedUser = localStorage.getItem('user');
    if (storedUser) {
        const parsedUser: User = JSON.parse(storedUser);
        user = parsedUser;
    }
}
export const userStore = {
    user,
    setUser (newUser: User) {
        this.user = newUser;
        localStorage.setItem('user', JSON.stringify(newUser));
    },
    clearUser() {
        this.user = null;
        localStorage.removeItem('user');
    }
}