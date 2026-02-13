import { apiRequest, type User, userStore } from '$lib/index';

export async function login(email: string, password: string): Promise<User> {
    const user: User = await apiRequest('/api/token', {
        method: 'POST',
        body: JSON.stringify({ email, password }),
    });
    userStore.setUser(user);

    return user;
    }

export async function logout(): Promise<void> {
    userStore.clearUser();
}