import { apiClient } from './api';
import { API_ENDPOINTS } from '@/constants/api.constants';
import { OAUTH_CALLBACK_URL, OAUTH_STATE_KEY, OAUTH_REDIRECT_KEY } from '@/constants/oauth.constants';
import { 
  OAuthURLRequest, 
  OAuthURLResponse, 
  OAuthCallbackResponse, 
  OAuthStatusResponse 
} from '@/types/oauth.types';
import { ApiResponse } from '@/types/api.types';

export class OAuthService {
  async getGoogleAuthUrl(redirectUri?: string): Promise<OAuthURLResponse> {
    const request: OAuthURLRequest = {
      provider: 'google',
      redirect_uri: redirectUri || `${window.location.origin}${OAUTH_CALLBACK_URL}`,
    };

    const response: ApiResponse<OAuthURLResponse> = await apiClient.get(
      API_ENDPOINTS.OAUTH_GOOGLE_URL,
      { params: { state: request.redirect_uri } }
    );

    // Store state for validation
    if (typeof window !== 'undefined') {
      localStorage.setItem(OAUTH_STATE_KEY, response.data.state);
    }

    return response.data;
  }

  async handleCallback(code: string, state: string): Promise<OAuthCallbackResponse> {
    // Validate state
    const storedState = typeof window !== 'undefined' 
      ? localStorage.getItem(OAUTH_STATE_KEY) 
      : null;
    
    if (storedState !== state) {
      throw new Error('Invalid OAuth state');
    }

    const response: ApiResponse<OAuthCallbackResponse> = await apiClient.get(
      API_ENDPOINTS.OAUTH_GOOGLE_CALLBACK,
      { 
        params: { 
          code, 
          state, 
          provider: 'google' 
        } 
      }
    );

    // Store token
    apiClient.setAuthTokenPublic(response.data.access_token);

    // Clean up stored state
    if (typeof window !== 'undefined') {
      localStorage.removeItem(OAUTH_STATE_KEY);
    }

    return response.data;
  }

  async revokeGoogleConnection(): Promise<void> {
    await apiClient.post(API_ENDPOINTS.OAUTH_GOOGLE_REVOKE);
  }

  async getOAuthStatus(): Promise<OAuthStatusResponse> {
    const response: ApiResponse<OAuthStatusResponse> = await apiClient.get(
      API_ENDPOINTS.OAUTH_STATUS
    );
    return response.data;
  }

  redirectToGoogleAuth(): void {
    this.getGoogleAuthUrl()
      .then(({ auth_url }) => {
        window.location.href = auth_url;
      })
      .catch((error) => {
        console.error('Failed to get Google auth URL:', error);
        throw error;
      });
  }

  isOAuthCallback(): boolean {
    if (typeof window === 'undefined') return false;
    
    const urlParams = new URLSearchParams(window.location.search);
    return urlParams.has('code') && urlParams.has('state');
  }

  getCallbackParams(): { code: string; state: string } | null {
    if (typeof window === 'undefined') return null;
    
    const urlParams = new URLSearchParams(window.location.search);
    const code = urlParams.get('code');
    const state = urlParams.get('state');
    
    if (code && state) {
      return { code, state };
    }
    
    return null;
  }
}

export const oauthService = new OAuthService();
export default oauthService;
