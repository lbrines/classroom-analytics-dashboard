'use client';

import { useEffect, useState } from 'react';
import { useRouter, useSearchParams } from 'next/navigation';
import { useOAuth } from '@/hooks/useOAuth';
import { useAuth } from '@/hooks/useAuth';

export default function OAuthCallbackPage() {
  const router = useRouter();
  const searchParams = useSearchParams();
  const { handleCallback } = useOAuth();
  const { refreshUser } = useAuth();
  const [status, setStatus] = useState<'loading' | 'success' | 'error'>('loading');
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    const processCallback = async () => {
      const code = searchParams.get('code');
      const state = searchParams.get('state');

      if (!code || !state) {
        setStatus('error');
        setError('Missing OAuth parameters');
        return;
      }

      try {
        await handleCallback(code, state);
        await refreshUser();
        setStatus('success');
        
        // Redirect to dashboard after successful OAuth
        setTimeout(() => {
          router.push('/dashboard');
        }, 2000);
      } catch (err: any) {
        setStatus('error');
        setError(err?.error?.message || 'OAuth callback failed');
      }
    };

    processCallback();
  }, [searchParams, handleCallback, refreshUser, router]);

  if (status === 'loading') {
    return (
      <div className="flex min-h-screen items-center justify-center">
        <div className="text-center">
          <div className="mx-auto h-8 w-8 animate-spin rounded-full border-4 border-primary-200 border-t-primary-600"></div>
          <p className="mt-2 text-sm text-secondary-600">Processing OAuth callback...</p>
        </div>
      </div>
    );
  }

  if (status === 'error') {
    return (
      <div className="flex min-h-screen items-center justify-center">
        <div className="text-center">
          <div className="mx-auto h-12 w-12 text-error-600">
            <svg fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-2.5L13.732 4c-.77-.833-1.964-.833-2.732 0L3.732 16.5c-.77.833.192 2.5 1.732 2.5z" />
            </svg>
          </div>
          <h1 className="mt-4 text-xl font-semibold text-error-600">OAuth Error</h1>
          <p className="mt-2 text-sm text-secondary-600">{error}</p>
          <button
            onClick={() => router.push('/login')}
            className="mt-4 rounded-md bg-primary-600 px-4 py-2 text-sm text-white hover:bg-primary-700"
          >
            Back to Login
          </button>
        </div>
      </div>
    );
  }

  return (
    <div className="flex min-h-screen items-center justify-center">
      <div className="text-center">
        <div className="mx-auto h-12 w-12 text-success-600">
          <svg fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M5 13l4 4L19 7" />
          </svg>
        </div>
        <h1 className="mt-4 text-xl font-semibold text-success-600">Success!</h1>
        <p className="mt-2 text-sm text-secondary-600">OAuth authentication successful. Redirecting to dashboard...</p>
      </div>
    </div>
  );
}
