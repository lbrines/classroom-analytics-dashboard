import { apiClient } from './api';
import { API_ENDPOINTS } from '@/constants/api.constants';
import { LoginRequest, LoginResponse, User } from '@/types/auth.types';
import { ApiResponse } from '@/types/api.types';

export class AuthService {
  async login(credentials: LoginRequest): Promise<LoginResponse> {
    const response: ApiResponse<LoginResponse> = await apiClient.post(
      API_ENDPOINTS.LOGIN,
      credentials
    );
    
    // Store token
    apiClient.setAuthToken(response.data.access_token);
    
    return response.data;
  }

  async logout(): Promise<void> {
    const token = this.getToken();
    if (token) {
      try {
        await apiClient.post(API_ENDPOINTS.LOGOUT, { token });
      } catch (error) {
        // Continue with logout even if API call fails
        console.warn('Logout API call failed:', error);
      }
    }
    
    // Clear local storage
    apiClient.clearAuth();
  }

  async getCurrentUser(): Promise<User> {
    const response: ApiResponse<User> = await apiClient.get(API_ENDPOINTS.ME);
    return response.data;
  }

  async refreshToken(): Promise<LoginResponse> {
    const token = this.getToken();
    if (!token) {
      throw new Error('No token available for refresh');
    }

    const response: ApiResponse<LoginResponse> = await apiClient.post(
      API_ENDPOINTS.REFRESH,
      { refresh_token: token }
    );
    
    // Update token
    apiClient.setAuthToken(response.data.access_token);
    
    return response.data;
  }

  getToken(): string | null {
    if (typeof window !== 'undefined') {
      return localStorage.getItem('auth_token');
    }
    return null;
  }

  isAuthenticated(): boolean {
    return !!this.getToken();
  }

  setToken(token: string): void {
    apiClient.setAuthToken(token);
  }
}

export const authService = new AuthService();
export default authService;
