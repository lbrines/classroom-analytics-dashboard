import React from 'react';
import { Card, CardContent } from '@/components/ui/Card';

interface ChartWidgetProps {
  title: string;
  children: React.ReactNode;
  actions?: React.ReactNode;
  loading?: boolean;
}

export function ChartWidget({
  title,
  children,
  actions,
  loading = false,
}: ChartWidgetProps) {
  if (loading) {
    return (
      <Card className="animate-pulse">
        <CardContent className="p-6">
          <div className="h-8 bg-secondary-100 rounded mb-4 w-1/3"></div>
          <div className="h-64 bg-secondary-100 rounded"></div>
        </CardContent>
      </Card>
    );
  }

  return (
    <Card>
      <CardContent className="p-6">
        <div className="flex items-center justify-between mb-4">
          <h3 className="text-lg font-semibold text-secondary-900">{title}</h3>
          {actions && <div>{actions}</div>}
        </div>
        <div className="mt-4">
          {children}
        </div>
      </CardContent>
    </Card>
  );
}

