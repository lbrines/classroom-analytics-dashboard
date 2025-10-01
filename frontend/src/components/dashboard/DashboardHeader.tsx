import React from 'react';
import { Button } from '@/components/ui/Button';
import { useAuth } from '@/hooks/useAuth';
import { useTranslation } from '@/hooks/useTranslation';
import { getInitials } from '@/lib/utils';

export function DashboardHeader() {
  const { user, logout } = useAuth();
  const { t } = useTranslation();

  const handleLogout = async () => {
    try {
      await logout();
    } catch (error) {
      console.error('Logout failed:', error);
    }
  };

  return (
    <header className="bg-white shadow-sm border-b border-secondary-200">
      <div className="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
        <div className="flex h-16 items-center justify-between">
          <div className="flex items-center">
            <div className="flex-shrink-0">
              <h1 className="text-xl font-bold text-primary-600">
                {t('auth.title')}
              </h1>
            </div>
            <nav className="ml-10 flex space-x-6">
              <a
                href="/dashboard"
                className="text-secondary-700 hover:text-primary-600 px-3 py-2 rounded-md text-sm font-medium transition-colors"
              >
                {t('navigation.dashboard')}
              </a>
              <a
                href="/search"
                className="text-secondary-500 hover:text-primary-600 px-3 py-2 rounded-md text-sm font-medium transition-colors"
              >
                Students
              </a>
              <a
                href="/courses"
                className="text-secondary-500 hover:text-primary-600 px-3 py-2 rounded-md text-sm font-medium transition-colors"
              >
                Courses
              </a>
              <a
                href="/reports"
                className="text-secondary-500 hover:text-primary-600 px-3 py-2 rounded-md text-sm font-medium transition-colors"
              >
                Reports
              </a>
            </nav>
          </div>

          <div className="flex items-center space-x-4">
            <div className="flex items-center space-x-3">
              <div className="h-8 w-8 rounded-full bg-primary-100 flex items-center justify-center">
                <span className="text-sm font-medium text-primary-700">
                  {user ? getInitials(user.name) : 'U'}
                </span>
              </div>
              <div className="hidden md:block">
                <p className="text-sm font-medium text-secondary-900">
                  {user?.name}
                </p>
                <p className="text-xs text-secondary-500">
                  {user?.role && t(`roles.${user.role}`)}
                </p>
              </div>
            </div>
            
            <Button
              variant="ghost"
              size="sm"
              onClick={handleLogout}
              className="text-secondary-500 hover:text-secondary-700"
            >
              {t('common.logout')}
            </Button>
          </div>
        </div>
      </div>
    </header>
  );
}
