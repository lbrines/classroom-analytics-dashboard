'use client';

import { useQuery } from '@tanstack/react-query';
import { apiClient } from '@/lib/api';
import { API_ENDPOINTS } from '@/constants/api.constants';
import { Course } from '@/types/course.types';

export function useCourses() {
  const { data, isLoading, error, refetch } = useQuery({
    queryKey: ['courses'],
    queryFn: async () => {
      try {
        const response = await apiClient.get(API_ENDPOINTS.COURSES);
        return (response.data as any).data as { courses: Course[]; total: number };
      } catch (err) {
        console.warn('Failed to fetch courses:', err);
        throw err; // Re-throw to let React Query handle the error state
      }
    },
    retry: false,
    staleTime: 5 * 60 * 1000, // 5 minutes
    gcTime: 10 * 60 * 1000, // 10 minutes
  });

  return {
    courses: data?.courses || [],
    total: data?.total || 0,
    isLoading,
    error,
    refetch,
  };
}

export function useCourse(courseId: string) {
  const { data, isLoading, error } = useQuery({
    queryKey: ['course', courseId],
    queryFn: async () => {
      const response = await apiClient.get(`${API_ENDPOINTS.COURSE}/${courseId}`);
      return (response.data as any).data as Course;
    },
    enabled: !!courseId,
  });

  return {
    course: data,
    isLoading,
    error,
  };
}

