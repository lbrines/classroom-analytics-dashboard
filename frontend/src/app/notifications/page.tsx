'use client';

import { AuthGuard } from '@/components/auth/AuthGuard';
import { DashboardHeader } from '@/components/dashboard/DashboardHeader';
import { NotificationCenter } from '@/components/notifications/NotificationCenter';

export default function NotificationsPage() {
  return (
    <AuthGuard>
      <div className="min-h-screen bg-secondary-50">
        <DashboardHeader />
        
        <main className="py-6">
          <div className="mx-auto max-w-4xl px-4 sm:px-6 lg:px-8">
            <div className="mb-8">
              <h1 className="text-3xl font-bold text-secondary-900">
                Notifications
              </h1>
              <p className="mt-2 text-sm text-secondary-600">
                Stay updated with your educational activities
              </p>
            </div>

            <NotificationCenter />
          </div>
        </main>
      </div>
    </AuthGuard>
  );
}

