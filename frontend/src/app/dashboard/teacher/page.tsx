'use client';

import { AuthGuard } from '@/components/auth/AuthGuard';
import { DashboardHeader } from '@/components/dashboard/DashboardHeader';
import { MetricCard } from '@/components/dashboard/MetricCard';
import { ChartWidget } from '@/components/dashboard/ChartWidget';
import { BarChart } from '@/components/charts/BarChart';
import { PieChart } from '@/components/charts/PieChart';
import { useMetrics } from '@/hooks/useMetrics';
import { useCourses } from '@/hooks/useCourses';
import { useAuth } from '@/hooks/useAuth';

export default function TeacherDashboard() {
  const { user } = useAuth();
  const { metrics, isLoading } = useMetrics();
  const { courses, isLoading: coursesLoading } = useCourses();

  // Redirect if not teacher
  if (user && user.role !== 'teacher') {
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
                Teacher Dashboard
              </h1>
              <p className="mt-2 text-sm text-secondary-600">
                Your courses and student performance
              </p>
            </div>

            {/* Key Metrics */}
            <div className="grid grid-cols-1 gap-6 sm:grid-cols-2 lg:grid-cols-3 mb-8">
              <MetricCard
                title="My Courses"
                value={metrics?.overview?.total_courses || 0}
                icon={<span className="text-3xl">📚</span>}
                loading={isLoading}
              />
              <MetricCard
                title="Total Students"
                value={metrics?.overview?.total_students || 0}
                icon={<span className="text-3xl">👥</span>}
                loading={isLoading}
              />
              <MetricCard
                title="Pending Reviews"
                value={metrics?.metrics?.pending_reviews || 0}
                change="Due this week"
                changeType="neutral"
                icon={<span className="text-3xl">📝</span>}
                loading={isLoading}
              />
            </div>

            {/* Charts */}
            <div className="grid grid-cols-1 gap-6 lg:grid-cols-2 mb-8">
              <ChartWidget title="Course Completion Rates" loading={isLoading}>
                <BarChart
                  categories={courses.slice(0, 3).map(c => c.name)}
                  series={[
                    { name: 'Completion', data: [85, 72, 68] },
                  ]}
                  height={300}
                  colors={['#10B981']}
                />
              </ChartWidget>

              <ChartWidget title="Grade Distribution" loading={isLoading}>
                <PieChart
                  labels={['A (9-10)', 'B (7-8.9)', 'C (5-6.9)', 'D (<5)']}
                  series={[35, 45, 15, 5]}
                  height={300}
                />
              </ChartWidget>
            </div>

            {/* Course List */}
            <div className="bg-white rounded-lg shadow p-6">
              <h3 className="text-lg font-semibold text-secondary-900 mb-4">
                My Courses
              </h3>
              <div className="space-y-3">
                {coursesLoading ? (
                  <div className="animate-pulse space-y-3">
                    {[1, 2, 3].map(i => (
                      <div key={i} className="h-16 bg-secondary-100 rounded"></div>
                    ))}
                  </div>
                ) : (
                  courses.map(course => (
                    <div 
                      key={course.id}
                      className="flex items-center justify-between p-4 border border-secondary-200 rounded-lg hover:bg-secondary-50 transition-colors"
                    >
                      <div>
                        <h4 className="font-semibold text-secondary-900">{course.name}</h4>
                        <p className="text-sm text-secondary-600">{course.section}</p>
                      </div>
                      <span className="px-3 py-1 bg-success-100 text-success-700 rounded-full text-xs font-medium">
                        {course.course_state}
                      </span>
                    </div>
                  ))
                )}
              </div>
            </div>
          </div>
        </main>
      </div>
    </AuthGuard>
  );
}

