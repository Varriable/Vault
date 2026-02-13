import {apiRequest} from './client';

export async function login(email: string, password: string): Promise<any> {
    const user = await apiRequest('/api/token', {
        method: 'POST',
        body: JSON.stringify({ email, password }),
    });
    localStorage.setItem('user', JSON.stringify(user));

    return user;
    }

