'use client';

import { AuthGuard } from '@/components/auth/AuthGuard';
import { DashboardHeader } from '@/components/dashboard/DashboardHeader';
import { MetricCard } from '@/components/dashboard/MetricCard';
import { ChartWidget } from '@/components/dashboard/ChartWidget';
import { BarChart } from '@/components/charts/BarChart';
import { LineChart } from '@/components/charts/LineChart';
import { Card, CardContent } from '@/components/ui/Card';
import { useMetrics } from '@/hooks/useMetrics';

export default function AdminDashboard() {
  const { metrics, isLoading } = useMetrics();

  return (
    <AuthGuard requiredRole="administrator">
      <div className="min-h-screen bg-secondary-50">
        <DashboardHeader />
        
        <main className="py-6">
          <div className="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
            <div className="mb-8">
              <h1 className="text-3xl font-bold text-secondary-900">
                Administrator Dashboard
              </h1>
              <p className="mt-2 text-sm text-secondary-600">
                System overview and global metrics
              </p>
            </div>

            {/* Key Metrics */}
            <div className="grid grid-cols-1 gap-6 sm:grid-cols-2 lg:grid-cols-4 mb-8">
              <MetricCard
                title="Total Courses"
                value={metrics?.overview?.total_courses || 0}
                change="+2 this month"
                changeType="positive"
                icon={<span className="text-3xl">📚</span>}
                loading={isLoading}
              />
              <MetricCard
                title="Active Students"
                value={metrics?.overview?.total_students || 0}
                change="+15%"
                changeType="positive"
                icon={<span className="text-3xl">👥</span>}
                loading={isLoading}
              />
              <MetricCard
                title="Total Teachers"
                value={metrics?.overview?.total_teachers || 0}
                change="Stable"
                changeType="neutral"
                icon={<span className="text-3xl">👨‍🏫</span>}
                loading={isLoading}
              />
              <MetricCard
                title="Engagement Score"
                value={`${metrics?.metrics?.engagement_score?.toFixed(1) || 0}%`}
                change="+5.2%"
                changeType="positive"
                icon={<span className="text-3xl">📈</span>}
                loading={isLoading}
              />
            </div>

            {/* Charts */}
            <div className="grid grid-cols-1 gap-6 lg:grid-cols-2 mb-8">
              <ChartWidget title="Course Performance" loading={isLoading}>
                {!isLoading && metrics ? (
                  <BarChart
                    categories={['eCommerce', 'Web Dev', 'Marketing']}
                    series={[
                      { name: 'Completion Rate', data: [85, 72, 68] },
                      { name: 'Average Grade', data: [89, 85, 82] },
                    ]}
                    height={300}
                  />
                ) : (
                  <div className="h-[300px] flex items-center justify-center text-secondary-500">
                    {isLoading ? 'Loading...' : 'No data available'}
                  </div>
                )}
              </ChartWidget>

              <ChartWidget title="Monthly Trends" loading={isLoading}>
                {!isLoading && metrics ? (
                  <LineChart
                    categories={['Aug', 'Sep', 'Oct', 'Nov', 'Dec']}
                    series={[
                      { name: 'Enrollments', data: [45, 52, 48, 55, 60] },
                      { name: 'Completions', data: [30, 35, 38, 42, 45] },
                    ]}
                    height={300}
                  />
                ) : (
                  <div className="h-[300px] flex items-center justify-center text-secondary-500">
                    {isLoading ? 'Loading...' : 'No data available'}
                  </div>
                )}
              </ChartWidget>
            </div>

            {/* System Stats */}
            <div className="grid grid-cols-1 gap-6 lg:grid-cols-3">
              <Card>
                <CardContent className="p-6">
                  <h3 className="text-lg font-semibold text-secondary-900 mb-4">
                    Quick Stats
                  </h3>
                  <dl className="space-y-3">
                    <div className="flex justify-between">
                      <dt className="text-sm text-secondary-600">Active Courses:</dt>
                      <dd className="text-sm font-semibold text-secondary-900">
                        {metrics?.overview?.active_courses || 0}
                      </dd>
                    </div>
                    <div className="flex justify-between">
                      <dt className="text-sm text-secondary-600">Avg Completion:</dt>
                      <dd className="text-sm font-semibold text-secondary-900">
                        {metrics?.metrics?.average_completion?.toFixed(1) || 0}%
                      </dd>
                    </div>
                    <div className="flex justify-between">
                      <dt className="text-sm text-secondary-600">Avg Grade:</dt>
                      <dd className="text-sm font-semibold text-secondary-900">
                        {metrics?.metrics?.average_grade?.toFixed(1) || 0}/10
                      </dd>
                    </div>
                  </dl>
                </CardContent>
              </Card>
            </div>
          </div>
        </main>
      </div>
    </AuthGuard>
  );
}

