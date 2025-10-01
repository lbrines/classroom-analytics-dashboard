'use client';

import { useQuery } from '@tanstack/react-query';
import { apiClient } from '@/lib/api';
import { API_ENDPOINTS } from '@/constants/api.constants';
import { DashboardMetrics } from '@/types/metrics.types';

export function useMetrics() {
  const { data, isLoading, error, refetch } = useQuery({
    queryKey: ['dashboard-metrics'],
    queryFn: async () => {
      try {
        const response = await apiClient.get(API_ENDPOINTS.DASHBOARD);
        return (response.data as any).data as DashboardMetrics;
      } catch (err) {
        console.warn('Failed to fetch dashboard metrics:', err);
        throw err; // Re-throw to let React Query handle the error state
      }
    },
    retry: false,
    staleTime: 5 * 60 * 1000, // 5 minutes
    gcTime: 10 * 60 * 1000, // 10 minutes
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
        const response = await apiClient.get(`${API_ENDPOINTS.DASHBOARD_ROLE}/${role}`);
        return (response.data as any).data as DashboardMetrics;
      } catch (err) {
        console.warn('Failed to fetch role metrics:', err);
        throw err; // Re-throw to let React Query handle the error state
      }
    },
    enabled: !!role,
    retry: false,
    staleTime: 5 * 60 * 1000, // 5 minutes
    gcTime: 10 * 60 * 1000, // 10 minutes
  });

  return {
    metrics: data || null,
    isLoading,
    error,
  };
}

