import { useMutation, useQuery, useQueryClient } from '@tanstack/react-query';
import { authService } from '@/lib/auth';
import { LoginRequest, User } from '@/types/auth.types';

export function useAuthQuery() {
  const queryClient = useQueryClient();

  const currentUserQuery = useQuery({
    queryKey: ['auth', 'currentUser'],
    queryFn: () => authService.getCurrentUser(),
    enabled: authService.isAuthenticated(),
    staleTime: 5 * 60 * 1000, // 5 minutes
  });

  const loginMutation = useMutation({
    mutationFn: (credentials: LoginRequest) => authService.login(credentials),
    onSuccess: (data) => {
      // Update the current user query with the logged-in user
      queryClient.setQueryData(['auth', 'currentUser'], data.user);
    },
    onError: () => {
      // Clear any cached user data on login error
      queryClient.removeQueries({ queryKey: ['auth', 'currentUser'] });
    },
  });

  const logoutMutation = useMutation({
    mutationFn: () => authService.logout(),
    onSuccess: () => {
      // Clear all auth-related queries
      queryClient.removeQueries({ queryKey: ['auth'] });
    },
  });

  const refreshTokenMutation = useMutation({
    mutationFn: () => authService.refreshToken(),
    onSuccess: (data) => {
      // Update the current user query with refreshed data
      queryClient.setQueryData(['auth', 'currentUser'], data.user);
    },
    onError: () => {
      // Clear auth data on refresh error
      queryClient.removeQueries({ queryKey: ['auth'] });
    },
  });

  return {
    currentUser: currentUserQuery.data,
    isAuthenticated: !!currentUserQuery.data,
    isLoading: currentUserQuery.isLoading || loginMutation.isPending || logoutMutation.isPending,
    error: currentUserQuery.error || loginMutation.error || logoutMutation.error,
    login: loginMutation.mutate,
    logout: logoutMutation.mutate,
    refreshToken: refreshTokenMutation.mutate,
    isLoginPending: loginMutation.isPending,
    isLogoutPending: logoutMutation.isPending,
  };
}
