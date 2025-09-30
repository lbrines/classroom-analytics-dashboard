import { useState, useEffect, useCallback } from 'react';
import { authService } from '@/lib/auth';
import { User, AuthState, LoginRequest } from '@/types/auth.types';

export function useAuth() {
  const [state, setState] = useState<AuthState>({
    user: null,
    token: null,
    isAuthenticated: false,
    isLoading: true,
    error: null,
  });

  const login = useCallback(async (credentials: LoginRequest) => {
    setState(prev => ({ ...prev, isLoading: true, error: null }));
    
    try {
      const response = await authService.login(credentials);
      setState({
        user: response.user,
        token: response.access_token,
        isAuthenticated: true,
        isLoading: false,
        error: null,
      });
      return response;
    } catch (error: any) {
      const errorMessage = error?.error?.message || 'Login failed';
      setState(prev => ({
        ...prev,
        isLoading: false,
        error: errorMessage,
      }));
      throw error;
    }
  }, []);

  const logout = useCallback(async () => {
    setState(prev => ({ ...prev, isLoading: true }));
    
    try {
      await authService.logout();
      setState({
        user: null,
        token: null,
        isAuthenticated: false,
        isLoading: false,
        error: null,
      });
    } catch (error) {
      console.error('Logout error:', error);
      // Still clear local state even if API call fails
      setState({
        user: null,
        token: null,
        isAuthenticated: false,
        isLoading: false,
        error: null,
      });
    }
  }, []);

  const refreshUser = useCallback(async () => {
    if (!authService.isAuthenticated()) {
      setState(prev => ({ ...prev, isLoading: false }));
      return;
    }

    setState(prev => ({ ...prev, isLoading: true }));
    
    try {
      const user = await authService.getCurrentUser();
      setState(prev => ({
        ...prev,
        user,
        isAuthenticated: true,
        isLoading: false,
        error: null,
      }));
    } catch (error: any) {
      console.error('Failed to refresh user:', error);
      setState({
        user: null,
        token: null,
        isAuthenticated: false,
        isLoading: false,
        error: 'Session expired',
      });
    }
  }, []);

  const clearError = useCallback(() => {
    setState(prev => ({ ...prev, error: null }));
  }, []);

  // Initialize auth state on mount
  useEffect(() => {
    const initAuth = async () => {
      if (authService.isAuthenticated()) {
        await refreshUser();
      } else {
        setState(prev => ({ ...prev, isLoading: false }));
      }
    };

    initAuth();
  }, [refreshUser]);

  return {
    ...state,
    login,
    logout,
    refreshUser,
    clearError,
  };
}
