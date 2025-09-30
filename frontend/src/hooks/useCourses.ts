'use client';

import { useQuery } from '@tanstack/react-query';
import { apiClient } from '@/lib/api';
import { Course } from '@/types/course.types';

export function useCourses() {
  const { data, isLoading, error, refetch } = useQuery({
    queryKey: ['courses'],
    queryFn: async () => {
      const response = await apiClient.get('/courses');
      return (response.data as any).data as { courses: Course[]; total: number };
    },
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
      const response = await apiClient.get(`/courses/${courseId}`);
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

