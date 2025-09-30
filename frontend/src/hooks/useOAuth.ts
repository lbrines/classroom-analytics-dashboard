import { useState, useCallback } from 'react';
import { oauthService } from '@/lib/oauth';
import { OAuthStatusResponse } from '@/types/oauth.types';

export function useOAuth() {
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [status, setStatus] = useState<OAuthStatusResponse | null>(null);

  const getGoogleAuthUrl = useCallback(async () => {
    setIsLoading(true);
    setError(null);
    
    try {
      const response = await oauthService.getGoogleAuthUrl();
      return response;
    } catch (error: any) {
      const errorMessage = error?.error?.message || 'Failed to get Google auth URL';
      setError(errorMessage);
      throw error;
    } finally {
      setIsLoading(false);
    }
  }, []);

  const handleCallback = useCallback(async (code: string, state: string) => {
    setIsLoading(true);
    setError(null);
    
    try {
      const response = await oauthService.handleCallback(code, state);
      return response;
    } catch (error: any) {
      const errorMessage = error?.error?.message || 'OAuth callback failed';
      setError(errorMessage);
      throw error;
    } finally {
      setIsLoading(false);
    }
  }, []);

  const revokeConnection = useCallback(async () => {
    setIsLoading(true);
    setError(null);
    
    try {
      await oauthService.revokeGoogleConnection();
      setStatus(prev => prev ? { ...prev, connected: false } : null);
    } catch (error: any) {
      const errorMessage = error?.error?.message || 'Failed to revoke connection';
      setError(errorMessage);
      throw error;
    } finally {
      setIsLoading(false);
    }
  }, []);

  const getStatus = useCallback(async () => {
    setIsLoading(true);
    setError(null);
    
    try {
      const response = await oauthService.getOAuthStatus();
      setStatus(response);
      return response;
    } catch (error: any) {
      const errorMessage = error?.error?.message || 'Failed to get OAuth status';
      setError(errorMessage);
      throw error;
    } finally {
      setIsLoading(false);
    }
  }, []);

  const redirectToGoogle = useCallback(() => {
    setIsLoading(true);
    setError(null);
    
    try {
      oauthService.redirectToGoogleAuth();
    } catch (error: any) {
      const errorMessage = error?.error?.message || 'Failed to redirect to Google';
      setError(errorMessage);
      setIsLoading(false);
    }
  }, []);

  const clearError = useCallback(() => {
    setError(null);
  }, []);

  return {
    isLoading,
    error,
    status,
    getGoogleAuthUrl,
    handleCallback,
    revokeConnection,
    getStatus,
    redirectToGoogle,
    clearError,
  };
}
