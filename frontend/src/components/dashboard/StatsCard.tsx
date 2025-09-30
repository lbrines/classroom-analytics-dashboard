import React from 'react';
import { Card, CardContent } from '@/components/ui/Card';
import { cn } from '@/lib/utils';

interface StatsCardProps {
  title: string;
  value: string | number;
  change?: string;
  changeType?: 'positive' | 'negative' | 'neutral';
  icon?: string;
  description?: string;
}

export function StatsCard({
  title,
  value,
  change,
  changeType = 'neutral',
  icon,
  description,
}: StatsCardProps) {
  const changeColors = {
    positive: 'text-success-600 bg-success-50',
    negative: 'text-error-600 bg-error-50',
    neutral: 'text-secondary-600 bg-secondary-50',
  };

  return (
    <Card className="hover:shadow-md transition-shadow">
      <CardContent className="p-6">
        <div className="flex items-center justify-between">
          <div className="flex-1">
            <p className="text-sm font-medium text-secondary-600">{title}</p>
            <p className="text-2xl font-bold text-secondary-900 mt-1">{value}</p>
            {change && (
              <div className="mt-2 flex items-center">
                <span
                  className={cn(
                    'inline-flex items-center px-2 py-1 rounded-full text-xs font-medium',
                    changeColors[changeType]
                  )}
                >
                  {changeType === 'positive' && (
                    <svg className="w-3 h-3 mr-1" fill="currentColor" viewBox="0 0 20 20">
                      <path fillRule="evenodd" d="M5.293 9.707a1 1 0 010-1.414l4-4a1 1 0 011.414 0l4 4a1 1 0 01-1.414 1.414L11 7.414V15a1 1 0 11-2 0V7.414L6.707 9.707a1 1 0 01-1.414 0z" clipRule="evenodd" />
                    </svg>
                  )}
                  {changeType === 'negative' && (
                    <svg className="w-3 h-3 mr-1" fill="currentColor" viewBox="0 0 20 20">
                      <path fillRule="evenodd" d="M14.707 10.293a1 1 0 010 1.414l-4 4a1 1 0 01-1.414 0l-4-4a1 1 0 111.414-1.414L9 12.586V5a1 1 0 012 0v7.586l2.293-2.293a1 1 0 011.414 0z" clipRule="evenodd" />
                    </svg>
                  )}
                  {change}
                </span>
              </div>
            )}
            {description && (
              <p className="text-xs text-secondary-500 mt-1">{description}</p>
            )}
          </div>
          {icon && (
            <div className="flex-shrink-0 ml-4">
              <div className="h-12 w-12 rounded-lg bg-primary-100 flex items-center justify-center">
                <span className="text-2xl">{icon}</span>
              </div>
            </div>
          )}
        </div>
      </CardContent>
    </Card>
  );
}
