'use client';

import React from 'react';
import { Card, CardContent } from '@/components/ui/Card';

interface SearchResultItem {
  id: string;
  entity_type: string;
  score: number;
  data: any;
  highlights?: any;
}

interface SearchResultsProps {
  results: SearchResultItem[];
  isLoading: boolean;
  totalResults: number;
  executionTime?: number;
}

export function SearchResults({ results, isLoading, totalResults, executionTime }: SearchResultsProps) {
  if (isLoading) {
    return (
      <div className="space-y-4">
        {[1, 2, 3].map(i => (
          <Card key={i} className="animate-pulse">
            <CardContent className="p-4">
              <div className="h-16 bg-secondary-100 rounded"></div>
            </CardContent>
          </Card>
        ))}
      </div>
    );
  }

  if (results.length === 0) {
    return (
      <Card>
        <CardContent className="p-8">
          <div className="text-center text-secondary-600">
            <svg className="mx-auto h-12 w-12 text-secondary-400" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z" />
            </svg>
            <h3 className="mt-2 text-sm font-medium">No results found</h3>
            <p className="mt-1 text-sm">Try a different search term</p>
          </div>
        </CardContent>
      </Card>
    );
  }

  return (
    <div className="space-y-4">
      <div className="flex items-center justify-between text-sm text-secondary-600">
        <p>
          Found <span className="font-semibold">{totalResults}</span> {totalResults === 1 ? 'result' : 'results'}
        </p>
        {executionTime && (
          <p className="text-xs">
            {executionTime.toFixed(0)}ms
          </p>
        )}
      </div>

      {results.map((result) => (
        <Card key={result.id} className="hover:shadow-md transition-shadow cursor-pointer">
          <CardContent className="p-4">
            <div className="flex items-start justify-between">
              <div className="flex-1">
                <div className="flex items-center space-x-2">
                  <h3 
                    className="text-lg font-semibold text-secondary-900"
                    dangerouslySetInnerHTML={{ 
                      __html: result.highlights?.name?.[0] || result.data.full_name || result.data.name 
                    }}
                  />
                  <span className="text-xs text-secondary-500">
                    ({(result.score * 100).toFixed(0)}% match)
                  </span>
                </div>
                {result.data.email_address && (
                  <p className="text-sm text-secondary-600 mt-1">
                    {result.data.email_address}
                  </p>
                )}
                {result.data.course_id && (
                  <p className="text-xs text-secondary-500 mt-2">
                    Course: {result.data.course_id}
                  </p>
                )}
              </div>
              <div className="ml-4">
                <span className="px-2 py-1 bg-primary-100 text-primary-700 rounded text-xs font-medium">
                  {result.entity_type}
                </span>
              </div>
            </div>
          </CardContent>
        </Card>
      ))}
    </div>
  );
}

