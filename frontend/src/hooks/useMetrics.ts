'use client';

import { useQuery } from '@tanstack/react-query';
import { apiClient } from '@/lib/api';
import { DashboardMetrics } from '@/types/metrics.types';

export function useMetrics() {
  const { data, isLoading, error, refetch } = useQuery({
    queryKey: ['dashboard-metrics'],
    queryFn: async () => {
      try {
        const response = await apiClient.get('/dashboard');
        return (response.data as any).data as DashboardMetrics;
      } catch (err) {
        console.warn('Failed to fetch dashboard metrics:', err);
        return null;
      }
    },
    retry: false,
  });

  return {
    metrics: data || null,
    isLoading,
    error,
    refetch,
  };
}

export function useRoleMetrics(role: string) {
  const { data, isLoading, error } = useQuery({
    queryKey: ['dashboard-metrics', role],
    queryFn: async () => {
      try {
        const response = await apiClient.get(`/dashboard/${role}`);
        return (response.data as any).data as DashboardMetrics;
      } catch (err) {
        console.warn('Failed to fetch role metrics:', err);
        return null;
      }
    },
    enabled: !!role,
    retry: false,
  });

  return {
    metrics: data || null,
    isLoading,
    error,
  };
}

