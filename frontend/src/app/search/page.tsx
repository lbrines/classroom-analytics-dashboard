'use client';

import { useState } from 'react';
import { AuthGuard } from '@/components/auth/AuthGuard';
import { DashboardHeader } from '@/components/dashboard/DashboardHeader';
import { SearchBar } from '@/components/search/SearchBar';
import { SearchResults } from '@/components/search/SearchResults';
import { useSearch } from '@/hooks/useSearch';

export default function SearchPage() {
  const { results, isLoading, executeSearch } = useSearch();

  const handleSearch = (query: string) => {
    if (query.trim()) {
      executeSearch(query);
    }
  };

  return (
    <AuthGuard>
      <div className="min-h-screen bg-secondary-50">
        <DashboardHeader />
        
        <main className="py-6">
          <div className="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
            <div className="mb-8">
              <h1 className="text-3xl font-bold text-secondary-900">
                Search Students
              </h1>
              <p className="mt-2 text-sm text-secondary-600">
                Find students by name, email, or ID
              </p>
            </div>

            <div className="mb-6">
              <SearchBar 
                onSearch={handleSearch} 
                placeholder="Search by name, email, or ID..."
                isLoading={isLoading}
              />
            </div>

            {results && (
              <SearchResults
                results={results.results || []}
                isLoading={isLoading}
                totalResults={results.total_results || 0}
                executionTime={results.execution_time_ms}
              />
            )}
          </div>
        </main>
      </div>
    </AuthGuard>
  );
}

