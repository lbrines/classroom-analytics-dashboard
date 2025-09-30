import { useState, useCallback } from 'react';
import { apiClient } from '@/lib/api';
import { ApiResponse, ApiError } from '@/types/api.types';

export function useApi<T = any>() {
  const [data, setData] = useState<T | null>(null);
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState<ApiError | null>(null);

  const request = useCallback(async (
    method: 'GET' | 'POST' | 'PUT' | 'DELETE',
    url: string,
    payload?: any,
    config?: any
  ) => {
    setIsLoading(true);
    setError(null);

    try {
      let response: ApiResponse<T>;
      
      switch (method) {
        case 'GET':
          response = await apiClient.get<T>(url, config);
          break;
        case 'POST':
          response = await apiClient.post<T>(url, payload, config);
          break;
        case 'PUT':
          response = await apiClient.put<T>(url, payload, config);
          break;
        case 'DELETE':
          response = await apiClient.delete<T>(url, config);
          break;
        default:
          throw new Error(`Unsupported method: ${method}`);
      }

      setData(response.data);
      return response;
    } catch (err: any) {
      setError(err);
      throw err;
    } finally {
      setIsLoading(false);
    }
  }, []);

  const get = useCallback((url: string, config?: any) => 
    request('GET', url, undefined, config), [request]);
  
  const post = useCallback((url: string, payload?: any, config?: any) => 
    request('POST', url, payload, config), [request]);
  
  const put = useCallback((url: string, payload?: any, config?: any) => 
    request('PUT', url, payload, config), [request]);
  
  const del = useCallback((url: string, config?: any) => 
    request('DELETE', url, undefined, config), [request]);

  const clearError = useCallback(() => {
    setError(null);
  }, []);

  const reset = useCallback(() => {
    setData(null);
    setError(null);
    setIsLoading(false);
  }, []);

  return {
    data,
    isLoading,
    error,
    get,
    post,
    put,
    delete: del,
    clearError,
    reset,
  };
}
