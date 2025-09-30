'use client';

import React, { createContext, useContext, useEffect } from 'react';
import { useAuth } from '@/hooks/useAuth';
import { useOAuth } from '@/hooks/useOAuth';
import { oauthService } from '@/lib/oauth';
import { useRouter } from 'next/navigation';

interface AuthContextType {
  auth: ReturnType<typeof useAuth>;
  oauth: ReturnType<typeof useOAuth>;
}

const AuthContext = createContext<AuthContextType | null>(null);

export function useAuthContext() {
  const context = useContext(AuthContext);
  if (!context) {
    throw new Error('useAuthContext must be used within an AuthProvider');
  }
  return context;
}

interface AuthProviderProps {
  children: React.ReactNode;
}

export function AuthProvider({ children }: AuthProviderProps) {
  const auth = useAuth();
  const oauth = useOAuth();
  const router = useRouter();

  // Handle OAuth callback on app initialization
  useEffect(() => {
    const handleOAuthCallback = async () => {
      if (oauthService.isOAuthCallback()) {
        const params = oauthService.getCallbackParams();
        if (params) {
          try {
            await oauth.handleCallback(params.code, params.state);
            await auth.refreshUser();
            router.push('/dashboard');
          } catch (error) {
            console.error('OAuth callback error:', error);
            router.push('/login?error=oauth_failed');
          }
        }
      }
    };

    handleOAuthCallback();
  }, [oauth, auth, router]);

  const value: AuthContextType = {
    auth,
    oauth,
  };

  return (
    <AuthContext.Provider value={value}>
      {children}
    </AuthContext.Provider>
  );
}
