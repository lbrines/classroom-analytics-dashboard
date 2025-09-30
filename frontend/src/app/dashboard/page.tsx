'use client';

import { AuthGuard } from '@/components/auth/AuthGuard';
import { DashboardHeader } from '@/components/dashboard/DashboardHeader';
import { StatsCard } from '@/components/dashboard/StatsCard';
import { useAuth } from '@/hooks/useAuth';
import { useTranslation } from '@/hooks/useTranslation';

export default function DashboardPage() {
  const { user } = useAuth();
  const { t } = useTranslation();

  return (
    <AuthGuard>
      <div className="min-h-screen bg-secondary-50">
        <DashboardHeader />
        
        <main className="py-6">
          <div className="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
            <div className="mb-8">
              <h1 className="text-2xl font-bold text-secondary-900">
                {t('dashboard.welcome', { name: user?.name || 'User' })}
              </h1>
              <p className="mt-1 text-sm text-secondary-600">
                {t('dashboard.overview')}
              </p>
            </div>

            <div className="grid grid-cols-1 gap-6 sm:grid-cols-2 lg:grid-cols-4">
              <StatsCard
                title="Total Students"
                value="150"
                change="+12%"
                changeType="positive"
                icon="👥"
              />
              <StatsCard
                title="Active Courses"
                value="8"
                change="+2"
                changeType="positive"
                icon="📚"
              />
              <StatsCard
                title="Assignments Due"
                value="23"
                change="-5"
                changeType="negative"
                icon="📝"
              />
              <StatsCard
                title="Completion Rate"
                value="87%"
                change="+3%"
                changeType="positive"
                icon="✅"
              />
            </div>

            <div className="mt-8">
              <div className="rounded-lg bg-white p-6 shadow">
                <h2 className="text-lg font-semibold text-secondary-900">
                  Recent Activity
                </h2>
                <div className="mt-4 space-y-4">
                  <div className="flex items-center space-x-3">
                    <div className="h-2 w-2 rounded-full bg-success-500"></div>
                    <p className="text-sm text-secondary-600">
                      New student registration: Ana Martinez
                    </p>
                    <span className="text-xs text-secondary-400">2 hours ago</span>
                  </div>
                  <div className="flex items-center space-x-3">
                    <div className="h-2 w-2 rounded-full bg-warning-500"></div>
                    <p className="text-sm text-secondary-600">
                      Assignment deadline approaching: Web Development Project
                    </p>
                    <span className="text-xs text-secondary-400">4 hours ago</span>
                  </div>
                  <div className="flex items-center space-x-3">
                    <div className="h-2 w-2 rounded-full bg-primary-500"></div>
                    <p className="text-sm text-secondary-600">
                      New course created: Advanced React
                    </p>
                    <span className="text-xs text-secondary-400">1 day ago</span>
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
