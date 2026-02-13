
export async function apiRequest<T>(endpoint: string, options?: RequestInit): Promise<T> {
  const baseUrl = import.meta.env.VITE_API_BASE_URL || '';
  const url = `${baseUrl}${endpoint}`;
  const retried = false;
  
  try {
    const response = await fetch(url, {
        headers: {
            'Content-Type': 'application/json',
            'credentials': 'include',
            },
            ...options,
        }
    )
    if (response.status === 401 && !retried) {
        // Attempt to refresh the token
        const refreshResponse = await fetch(`${baseUrl}/auth/refresh`, {
            method: 'POST',
            credentials: 'include',
        });
        
        if (refreshResponse.ok) {
            // Retry the original request
            return await apiRequest<T>(endpoint, options);
        } else {
            throw new Error('Unauthorized and token refresh failed');
        }
    }
    
    if (!response.ok) {
      const errorText = await response.text();
      throw new Error(`API request failed: ${response.status} ${response.statusText} - ${errorText}`);
    }
    
    return await response.json() as T;
  } catch (error) {
    console.error('API request error:', error);
    throw error;
  }
  

}