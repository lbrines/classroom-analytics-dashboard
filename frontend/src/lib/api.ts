import axios, { AxiosInstance, AxiosRequestConfig, AxiosResponse } from 'axios';
import { API_BASE_URL, HTTP_STATUS, ERROR_CODES } from '@/constants/api.constants';
import { ApiResponse, ApiError } from '@/types/api.types';

class ApiClient {
  private client: AxiosInstance;

  constructor() {
    this.client = axios.create({
      baseURL: API_BASE_URL,
      timeout: 10000,
      headers: {
        'Content-Type': 'application/json',
      },
    });

    this.setupInterceptors();
  }

  private setupInterceptors() {
    // Request interceptor
    this.client.interceptors.request.use(
      (config) => {
        // Add auth token if available
        const token = this.getAuthToken();
        if (token) {
          config.headers.Authorization = `Bearer ${token}`;
        }
        return config;
      },
      (error) => {
        return Promise.reject(error);
      }
    );

    // Response interceptor
    this.client.interceptors.response.use(
      (response: AxiosResponse<ApiResponse>) => {
        return response;
      },
      (error) => {
        if (error.response?.status === HTTP_STATUS.UNAUTHORIZED) {
          // Handle unauthorized access
          this.clearAuthToken();
          window.location.href = '/login';
        }
        return Promise.reject(this.handleError(error));
      }
    );
  }

  private getAuthToken(): string | null {
    if (typeof window !== 'undefined') {
      return localStorage.getItem('auth_token');
    }
    return null;
  }

  private setAuthToken(token: string): void {
    if (typeof window !== 'undefined') {
      localStorage.setItem('auth_token', token);
    }
  }

  private clearAuthToken(): void {
    if (typeof window !== 'undefined') {
      localStorage.removeItem('auth_token');
    }
  }

  private handleError(error: any): ApiError {
    if (error.response?.data) {
      return error.response.data;
    }

    if (error.code === 'ECONNABORTED') {
      return {
        error: {
          code: ERROR_CODES.NETWORK_ERROR,
          message: 'Request timeout',
        },
        meta: {
          timestamp: new Date().toISOString(),
          version: '1.0.0',
          request_id: '',
        },
      };
    }

    return {
      error: {
        code: ERROR_CODES.SERVER_ERROR,
        message: 'An unexpected error occurred',
      },
      meta: {
        timestamp: new Date().toISOString(),
        version: '1.0.0',
        request_id: '',
      },
    };
  }

  public setAuthToken(token: string): void {
    this.setAuthToken(token);
  }

  public clearAuth(): void {
    this.clearAuthToken();
  }

  public async get<T>(url: string, config?: AxiosRequestConfig): Promise<ApiResponse<T>> {
    const response = await this.client.get<ApiResponse<T>>(url, config);
    return response.data;
  }

  public async post<T>(url: string, data?: any, config?: AxiosRequestConfig): Promise<ApiResponse<T>> {
    const response = await this.client.post<ApiResponse<T>>(url, data, config);
    return response.data;
  }

  public async put<T>(url: string, data?: any, config?: AxiosRequestConfig): Promise<ApiResponse<T>> {
    const response = await this.client.put<ApiResponse<T>>(url, data, config);
    return response.data;
  }

  public async delete<T>(url: string, config?: AxiosRequestConfig): Promise<ApiResponse<T>> {
    const response = await this.client.delete<ApiResponse<T>>(url, config);
    return response.data;
  }
}

export const apiClient = new ApiClient();
export default apiClient;
