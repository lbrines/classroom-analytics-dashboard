'use client';

import { AuthGuard } from '@/components/auth/AuthGuard';
import { DashboardHeader } from '@/components/dashboard/DashboardHeader';
import { CourseList } from '@/components/google/CourseList';

export default function CoursesPage() {
  return (
    <AuthGuard>
      <div className="min-h-screen bg-secondary-50">
        <DashboardHeader />
        
        <main className="py-6">
          <div className="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
            <div className="mb-8">
              <h1 className="text-3xl font-bold text-secondary-900">
                Courses
              </h1>
              <p className="mt-2 text-sm text-secondary-600">
                Browse and manage your courses
              </p>
            </div>

            <CourseList />
          </div>
        </main>
      </div>
    </AuthGuard>
  );
}

