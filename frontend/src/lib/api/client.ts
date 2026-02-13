
export async function apiRequest<T>(endpoint: string, options?: RequestInit): Promise<T> {
  const baseUrl = import.meta.env.VITE_API_BASE_URL || '';
  const url = `${baseUrl}${endpoint}`;
  let isRetried = false
  
  try {
    const response = await fetch(url, {
        credentials: 'include', 
        headers: {
            'Content-Type': 'application/json',
            },
            ...options,
        }
    )

    if (response.status === 401) {
      if (isRetried) {
        await fetch(`${baseUrl}/v1/user/logout/`, {
          method: 'POST',
          credentials: 'include',
          headers: {
            'Content-Type': 'application/json',
          },
        });
        throw new Error('Unauthorized: Please log in to access this resource.');
      }
      isRetried = true;
      try {
        const refreshResponse = await fetch(`${baseUrl}/v1/user/refresh/`, {
          method: 'POST',
          credentials: 'include',
          headers: {
            'Content-Type': 'application/json',
          },
        });
        if (!refreshResponse.ok) {
          throw new Error('Session refresh failed. Please log in again.');
        }
      }
      catch (refreshError) {
        console.error('Session refresh error:', refreshError);
        throw new Error('Session refresh failed. Please log in again.');
      }
      return await apiRequest<T>(endpoint, options);
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