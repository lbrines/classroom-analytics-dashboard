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

