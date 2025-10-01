'use client';

import { AuthGuard } from '@/components/auth/AuthGuard';
import { DashboardHeader } from '@/components/dashboard/DashboardHeader';
import { MetricCard } from '@/components/dashboard/MetricCard';
import { ChartWidget } from '@/components/dashboard/ChartWidget';
import { BarChart } from '@/components/charts/BarChart';
import { LineChart } from '@/components/charts/LineChart';
import { PieChart } from '@/components/charts/PieChart';
import { Card, CardContent } from '@/components/ui/Card';
import { useMetrics } from '@/hooks/useMetrics';

export default function CoordinatorDashboard() {
  const { metrics, isLoading } = useMetrics();

  return (
    <AuthGuard requiredRole="coordinator">
      <div className="min-h-screen bg-secondary-50">
        <DashboardHeader />
        
        <main className="py-6">
          <div className="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
            <div className="mb-8">
              <h1 className="text-3xl font-bold text-secondary-900">
                Coordinator Dashboard
              </h1>
              <p className="mt-2 text-sm text-secondary-600">
                Program oversight and teacher management
              </p>
            </div>

            {/* Key Metrics */}
            <div className="grid grid-cols-1 gap-6 sm:grid-cols-2 lg:grid-cols-4 mb-8">
              <MetricCard
                title="Programs Managed"
                value={metrics?.overview?.total_courses || 0}
                change="+2 this quarter"
                changeType="positive"
                icon={<span className="text-3xl">📚</span>}
                loading={isLoading}
              />
              <MetricCard
                title="Active Teachers"
                value={metrics?.overview?.total_teachers || 0}
                change="Stable"
                changeType="neutral"
                icon={<span className="text-3xl">👨‍🏫</span>}
                loading={isLoading}
              />
              <MetricCard
                title="Total Students"
                value={metrics?.overview?.total_students || 0}
                change="+12%"
                changeType="positive"
                icon={<span className="text-3xl">👥</span>}
                loading={isLoading}
              />
              <MetricCard
                title="Avg Completion"
                value={`${metrics?.metrics?.average_completion?.toFixed(1) || 0}%`}
                change="+3.2%"
                changeType="positive"
                icon={<span className="text-3xl">📊</span>}
                loading={isLoading}
              />
            </div>

            {/* Charts */}
            <div className="grid grid-cols-1 gap-6 lg:grid-cols-2 mb-8">
              <ChartWidget title="Teacher Performance Comparison" loading={isLoading}>
                {!isLoading && metrics ? (
                  <BarChart
                    categories={['Teacher A', 'Teacher B', 'Teacher C', 'Teacher D']}
                    series={[
                      { name: 'Completion Rate', data: [85, 72, 78, 68] },
                      { name: 'Average Grade', data: [89, 82, 85, 80] },
                    ]}
                    height={300}
                  />
                ) : (
                  <div className="h-[300px] flex items-center justify-center text-secondary-500">
                    {isLoading ? 'Loading...' : 'No data available'}
                  </div>
                )}
              </ChartWidget>

              <ChartWidget title="Program Enrollment Trends" loading={isLoading}>
                {!isLoading && metrics ? (
                  <LineChart
                    categories={['Aug', 'Sep', 'Oct', 'Nov', 'Dec']}
                    series={[
                      { name: 'eCommerce', data: [145, 150, 148, 152, 158] },
                      { name: 'Marketing', data: [138, 142, 145, 148, 150] },
                    ]}
                    height={300}
                    colors={['#3B82F6', '#10B981']}
                  />
                ) : (
                  <div className="h-[300px] flex items-center justify-center text-secondary-500">
                    {isLoading ? 'Loading...' : 'No data available'}
                  </div>
                )}
              </ChartWidget>

              <ChartWidget title="Student Progress Distribution" loading={isLoading}>
                {!isLoading && metrics ? (
                  <PieChart
                    labels={['On Track', 'At Risk', 'Excelling', 'Needs Attention']}
                    series={[60, 20, 15, 5]}
                    height={300}
                    colors={['#10B981', '#F59E0B', '#3B82F6', '#EF4444']}
                  />
                ) : (
                  <div className="h-[300px] flex items-center justify-center text-secondary-500">
                    {isLoading ? 'Loading...' : 'No data available'}
                  </div>
                )}
              </ChartWidget>

              <ChartWidget title="Program Completion by Cohort" loading={isLoading}>
                {!isLoading && metrics ? (
                  <BarChart
                    categories={['Cohort Q1', 'Cohort Q2', 'Cohort Q3', 'Cohort Q4']}
                    series={[
                      { name: 'Completed', data: [85, 78, 82, 70] },
                    ]}
                    height={300}
                    colors={['#10B981']}
                  />
                ) : (
                  <div className="h-[300px] flex items-center justify-center text-secondary-500">
                    {isLoading ? 'Loading...' : 'No data available'}
                  </div>
                )}
              </ChartWidget>
            </div>

            {/* Teacher Overview */}
            <div className="grid grid-cols-1 gap-6 lg:grid-cols-2">
              <Card>
                <CardContent className="p-6">
                  <h3 className="text-lg font-semibold text-secondary-900 mb-4">
                    Teacher Performance
                  </h3>
                  <div className="space-y-4">
                    <div className="flex items-center justify-between pb-3 border-b border-secondary-100">
                      <div className="flex items-center space-x-3">
                        <div className="h-10 w-10 rounded-full bg-primary-100 flex items-center justify-center">
                          <span className="text-sm font-medium text-primary-700">CR</span>
                        </div>
                        <div>
                          <p className="text-sm font-medium text-secondary-900">Carlos Rodriguez</p>
                          <p className="text-xs text-secondary-600">eCommerce Specialist</p>
                        </div>
                      </div>
                      <div className="text-right">
                        <p className="text-sm font-semibold text-success-700">85%</p>
                        <p className="text-xs text-secondary-600">Completion</p>
                      </div>
                    </div>
                    <div className="flex items-center justify-between pb-3 border-b border-secondary-100">
                      <div className="flex items-center space-x-3">
                        <div className="h-10 w-10 rounded-full bg-primary-100 flex items-center justify-center">
                          <span className="text-sm font-medium text-primary-700">AM</span>
                        </div>
                        <div>
                          <p className="text-sm font-medium text-secondary-900">Ana Martinez</p>
                          <p className="text-xs text-secondary-600">Digital Marketing</p>
                        </div>
                      </div>
                      <div className="text-right">
                        <p className="text-sm font-semibold text-success-700">78%</p>
                        <p className="text-xs text-secondary-600">Completion</p>
                      </div>
                    </div>
                  </div>
                </CardContent>
              </Card>

              <Card>
                <CardContent className="p-6">
                  <h3 className="text-lg font-semibold text-secondary-900 mb-4">
                    Program Stats
                  </h3>
                  <dl className="space-y-3">
                    <div className="flex justify-between">
                      <dt className="text-sm text-secondary-600">Active Programs:</dt>
                      <dd className="text-sm font-semibold text-secondary-900">
                        {metrics?.overview?.total_courses || 0}
                      </dd>
                    </div>
                    <div className="flex justify-between">
                      <dt className="text-sm text-secondary-600">Enrolled Students:</dt>
                      <dd className="text-sm font-semibold text-secondary-900">
                        {metrics?.overview?.total_students || 0}
                      </dd>
                    </div>
                    <div className="flex justify-between">
                      <dt className="text-sm text-secondary-600">Avg Grade:</dt>
                      <dd className="text-sm font-semibold text-secondary-900">
                        {metrics?.metrics?.average_grade?.toFixed(1) || 0}/10
                      </dd>
                    </div>
                    <div className="flex justify-between">
                      <dt className="text-sm text-secondary-600">At-Risk Students:</dt>
                      <dd className="text-sm font-semibold text-danger-700">
                        {Math.floor((metrics?.overview?.total_students || 0) * 0.05)}
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

