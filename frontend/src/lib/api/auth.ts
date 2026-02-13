import { apiRequest, type User, userStore } from '$lib/index';

export async function login(email: string, password: string): Promise<User> {
    const user: User = await apiRequest('/v1/user/login/', {
        method: 'POST',
        body: JSON.stringify({ email, password }),
    });
    userStore.setUser(user);

    return user;
}

export async function register(name: string, email: string, password: string): Promise<User> {
    const user: User = await apiRequest('/v1/user/create/', {
        method: 'POST',
        body: JSON.stringify({ email, password }),
    });
    userStore.setUser(user);

    return user;
}

export async function logout(): Promise<void> {
    await apiRequest('/v1/user/logout/', {
        method: 'POST',
    });
    userStore.clearUser();
}