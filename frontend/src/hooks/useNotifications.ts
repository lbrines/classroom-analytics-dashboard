'use client';

import { useQuery, useMutation, useQueryClient } from '@tanstack/react-query';
import { apiClient } from '@/lib/api';

interface Notification {
  id: string;
  user_id: string;
  type: string;
  priority: string;
  title: string;
  message: string;
  data?: any;
  read: boolean;
  created_at: string;
  expires_at?: string;
}

interface NotificationList {
  notifications: Notification[];
  total: number;
  unread_count: number;
}

export function useNotifications(unreadOnly: boolean = false) {
  const queryClient = useQueryClient();

  const { data, isLoading, error, refetch } = useQuery({
    queryKey: ['notifications', unreadOnly],
    queryFn: async () => {
      const response = await apiClient.get(`/notifications?unread_only=${unreadOnly}`);
      return (response.data as any).data as NotificationList;
    },
  });

  const markAsReadMutation = useMutation({
    mutationFn: async (notificationId: string) => {
      const response = await apiClient.put(`/notifications/${notificationId}/read`);
      return (response.data as any).data;
    },
    onSuccess: () => {
      // Refetch notifications after marking as read
      queryClient.invalidateQueries({ queryKey: ['notifications'] });
    },
  });

  return {
    notifications: data?.notifications || [],
    total: data?.total || 0,
    unreadCount: data?.unread_count || 0,
    isLoading,
    error,
    refetch,
    markAsRead: markAsReadMutation.mutate,
    isMarkingAsRead: markAsReadMutation.isPending,
  };
}

export function useNotificationPreferences() {
  const queryClient = useQueryClient();

  const { data, isLoading, error, refetch } = useQuery({
    queryKey: ['notification-preferences'],
    queryFn: async () => {
      try {
        const response = await apiClient.get(`/notifications/preferences`);
        return (response.data as any).data;
      } catch (err) {
        console.warn('Failed to fetch notification preferences:', err);
        return null;
      }
    },
    retry: false,
    staleTime: 5 * 60 * 1000, // 5 minutes
  });

  const updatePreferencesMutation = useMutation({
    mutationFn: async (preferences: any) => {
      const response = await apiClient.put(`/notifications/preferences`, preferences);
      return (response.data as any).data;
    },
    onSuccess: () => {
      // Invalidate and refetch preferences
      queryClient.invalidateQueries({ queryKey: ['notification-preferences'] });
    },
  });

  return {
    preferences: data,
    isLoading,
    error,
    updatePreferences: updatePreferencesMutation.mutateAsync,
    isUpdating: updatePreferencesMutation.isPending,
    refetch,
  };
}

