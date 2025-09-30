import { useMutation, useQuery, useQueryClient } from '@tanstack/react-query';
import { oauthService } from '@/lib/oauth';
import { OAuthStatusResponse } from '@/types/oauth.types';

export function useOAuthQuery() {
  const queryClient = useQueryClient();

  const oauthStatusQuery = useQuery({
    queryKey: ['oauth', 'status'],
    queryFn: () => oauthService.getOAuthStatus(),
    enabled: false, // Only fetch when explicitly requested
    staleTime: 2 * 60 * 1000, // 2 minutes
  });

  const getGoogleAuthUrlMutation = useMutation({
    mutationFn: (redirectUri?: string) => oauthService.getGoogleAuthUrl(redirectUri),
  });

  const handleCallbackMutation = useMutation({
    mutationFn: ({ code, state }: { code: string; state: string }) =>
      oauthService.handleCallback(code, state),
    onSuccess: () => {
      // Invalidate auth queries to refresh user data
      queryClient.invalidateQueries({ queryKey: ['auth'] });
    },
  });

  const revokeConnectionMutation = useMutation({
    mutationFn: () => oauthService.revokeGoogleConnection(),
    onSuccess: () => {
      // Update OAuth status
      queryClient.setQueryData(['oauth', 'status'], (old: OAuthStatusResponse) => ({
        ...old,
        connected: false,
        provider: null,
        user_info: null,
      }));
    },
  });

  const getStatusMutation = useMutation({
    mutationFn: () => oauthService.getOAuthStatus(),
    onSuccess: (data) => {
      queryClient.setQueryData(['oauth', 'status'], data);
    },
  });

  return {
    status: oauthStatusQuery.data,
    isLoading: oauthStatusQuery.isLoading || 
               getGoogleAuthUrlMutation.isPending || 
               handleCallbackMutation.isPending || 
               revokeConnectionMutation.isPending ||
               getStatusMutation.isPending,
    error: oauthStatusQuery.error || 
           getGoogleAuthUrlMutation.error || 
           handleCallbackMutation.error || 
           revokeConnectionMutation.error ||
           getStatusMutation.error,
    getGoogleAuthUrl: getGoogleAuthUrlMutation.mutate,
    handleCallback: handleCallbackMutation.mutate,
    revokeConnection: revokeConnectionMutation.mutate,
    getStatus: getStatusMutation.mutate,
    isGetUrlPending: getGoogleAuthUrlMutation.isPending,
    isCallbackPending: handleCallbackMutation.isPending,
    isRevokePending: revokeConnectionMutation.isPending,
    isStatusPending: getStatusMutation.isPending,
  };
}
