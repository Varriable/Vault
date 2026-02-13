import { apiRequest, type Secret } from '$lib/index';

export async function getSecrets(): Promise<Secret[]> {
    return await apiRequest('/v1/secrets/my-secrets/');
}

export async function createSecret(title: string, key: string): Promise<Secret> {
    return await apiRequest('/v1/secrets/create/', {
        method: 'POST',
        body: JSON.stringify({ title, key }),
    });
}

export async function updateSecret(id: number, title: string, key: string): Promise<Secret> {
    return await apiRequest(`/v1/secrets/${id}/edit/`, {
        method: 'PUT',
        body: JSON.stringify({ title, key }),
    });
}

export async function deleteSecret(id: number): Promise<void> {
    await apiRequest(`/v1/secrets/${id}/delete/`, {
        method: 'DELETE',
    });
}