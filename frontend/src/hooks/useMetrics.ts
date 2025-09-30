'use client';

import { useQuery } from '@tanstack/react-query';
import { apiClient } from '@/lib/api';
import { DashboardMetrics } from '@/types/metrics.types';

export function useMetrics() {
  const { data, isLoading, error, refetch } = useQuery({
    queryKey: ['dashboard-metrics'],
    queryFn: async () => {
      const response = await apiClient.get('/metrics/dashboard');
      return (response.data as any).data as DashboardMetrics;
    },
  });

  return {
    metrics: data,
    isLoading,
    error,
    refetch,
  };
}

export function useRoleMetrics(role: string) {
  const { data, isLoading, error } = useQuery({
    queryKey: ['dashboard-metrics', role],
    queryFn: async () => {
      const response = await apiClient.get(`/metrics/dashboard/${role}`);
      return (response.data as any).data as DashboardMetrics;
    },
    enabled: !!role,
  });

  return {
    metrics: data,
    isLoading,
    error,
  };
}

