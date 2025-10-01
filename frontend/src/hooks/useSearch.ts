'use client';

import { useState } from 'react';
import { useQuery, useMutation } from '@tanstack/react-query';
import { apiClient } from '@/lib/api';

interface SearchResult {
  query: string;
  entity_type: string;
  total_results: number;
  page: number;
  page_size: number;
  total_pages: number;
  results: any[];
  execution_time_ms?: number;
}

export function useSearch() {
  const [searchQuery, setSearchQuery] = useState('');
  const [page, setPage] = useState(1);

  const searchMutation = useMutation({
    mutationFn: async (params: { query: string; entity_type?: string; page?: number }) => {
      const response = await apiClient.post('/search', {
        query: params.query,
        entity_type: params.entity_type || 'student',
        page: params.page || 1,
        page_size: 10,
      });
      return (response.data as any).data as SearchResult;
    },
  });

  const executeSearch = (query: string, entityType: string = 'student', pageNum: number = 1) => {
    setSearchQuery(query);
    setPage(pageNum);
    searchMutation.mutate({ query, entity_type: entityType, page: pageNum });
  };

  return {
    searchQuery,
    page,
    results: searchMutation.data,
    isLoading: searchMutation.isPending,
    error: searchMutation.error,
    executeSearch,
    setPage,
  };
}

