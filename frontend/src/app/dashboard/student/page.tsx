'use client';

import { AuthGuard } from '@/components/auth/AuthGuard';
import { DashboardHeader } from '@/components/dashboard/DashboardHeader';
import { MetricCard } from '@/components/dashboard/MetricCard';
import { ChartWidget } from '@/components/dashboard/ChartWidget';
import { LineChart } from '@/components/charts/LineChart';
import { PieChart } from '@/components/charts/PieChart';
import { useMetrics } from '@/hooks/useMetrics';
import { useAuth } from '@/hooks/useAuth';

export default function StudentDashboard() {
  const { user } = useAuth();
  const { metrics, isLoading } = useMetrics();

  // Redirect if not student
  if (user && user.role !== 'student') {
    window.location.href = '/dashboard';
    return null;
  }

  return (
    <AuthGuard>
      <div className="min-h-screen bg-secondary-50">
        <DashboardHeader />
        
        <main className="py-6">
          <div className="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
            <div className="mb-8">
              <h1 className="text-3xl font-bold text-secondary-900">
                My Learning Dashboard
              </h1>
              <p className="mt-2 text-sm text-secondary-600">
                Track your progress and achievements
              </p>
            </div>

            {/* Key Metrics */}
            <div className="grid grid-cols-1 gap-6 sm:grid-cols-2 lg:grid-cols-4 mb-8">
              <MetricCard
                title="Overall Progress"
                value={`${metrics?.overview?.overall_progress?.toFixed(0) || 0}%`}
                change="+5% this week"
                changeType="positive"
                icon={<span className="text-3xl">📊</span>}
                loading={isLoading}
              />
              <MetricCard
                title="Average Grade"
                value={`${metrics?.metrics?.average_grade?.toFixed(1) || 0}/10`}
                change="+0.3"
                changeType="positive"
                icon={<span className="text-3xl">⭐</span>}
                loading={isLoading}
              />
              <MetricCard
                title="Courses Enrolled"
                value={metrics?.overview?.courses_enrolled || 0}
                icon={<span className="text-3xl">📚</span>}
                loading={isLoading}
              />
              <MetricCard
                title="Learning Streak"
                value={`${metrics?.metrics?.streak_days || 0} days`}
                change="Keep it up!"
                changeType="positive"
                icon={<span className="text-3xl">🔥</span>}
                loading={isLoading}
              />
            </div>

            {/* Charts */}
            <div className="grid grid-cols-1 gap-6 lg:grid-cols-2 mb-8">
              <ChartWidget title="Your Progress Over Time" loading={isLoading}>
                {!isLoading && metrics ? (
                  <LineChart
                    categories={['Week 1', 'Week 2', 'Week 3', 'Week 4']}
                    series={[
                      { name: 'Progress', data: [45, 60, 75, 85] },
                      { name: 'Target', data: [50, 60, 70, 80] },
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

              <ChartWidget title="Assignment Status" loading={isLoading}>
                {!isLoading && metrics ? (
                  <PieChart
                    labels={['Completed', 'In Progress', 'Pending']}
                    series={[
                      metrics?.metrics?.completed_assignments || 28,
                      8,
                      metrics?.overview?.pending_assignments || 12
                    ]}
                    height={300}
                    colors={['#10B981', '#F59E0B', '#EF4444']}
                  />
                ) : (
                  <div className="h-[300px] flex items-center justify-center text-secondary-500">
                    {isLoading ? 'Loading...' : 'No data available'}
                  </div>
                )}
              </ChartWidget>
            </div>

            {/* Recent Activity */}
            <div className="bg-white rounded-lg shadow p-6">
              <h3 className="text-lg font-semibold text-secondary-900 mb-4">
                Recent Activity
              </h3>
              <div className="space-y-4">
                <div className="flex items-start space-x-3 pb-4 border-b border-secondary-100">
                  <div className="h-10 w-10 rounded-full bg-success-100 flex items-center justify-center flex-shrink-0">
                    <span className="text-xl">✅</span>
                  </div>
                  <div className="flex-1">
                    <p className="text-sm font-medium text-secondary-900">
                      Assignment submitted
                    </p>
                    <p className="text-xs text-secondary-600 mt-1">
                      eCommerce Specialist - Module 3 Project
                    </p>
                    <p className="text-xs text-secondary-400 mt-1">2 hours ago</p>
                  </div>
                </div>
                <div className="flex items-start space-x-3 pb-4 border-b border-secondary-100">
                  <div className="h-10 w-10 rounded-full bg-primary-100 flex items-center justify-center flex-shrink-0">
                    <span className="text-xl">📚</span>
                  </div>
                  <div className="flex-1">
                    <p className="text-sm font-medium text-secondary-900">
                      New lesson available
                    </p>
                    <p className="text-xs text-secondary-600 mt-1">
                      Web Development - React Hooks
                    </p>
                    <p className="text-xs text-secondary-400 mt-1">1 day ago</p>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </main>
      </div>
    </AuthGuard>
  );
}

