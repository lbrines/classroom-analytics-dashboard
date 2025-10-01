'use client';

import React from 'react';
import { Card, CardContent } from '@/components/ui/Card';
import { useNotifications } from '@/hooks/useNotifications';

export function NotificationCenter() {
  const { notifications, unreadCount, isLoading, markAsRead } = useNotifications();

  const handleMarkAsRead = (notificationId: string) => {
    markAsRead(notificationId);
  };

  if (isLoading) {
    return (
      <Card>
        <CardContent className="p-6">
          <div className="animate-pulse space-y-4">
            {[1, 2, 3].map(i => (
              <div key={i} className="h-20 bg-secondary-100 rounded"></div>
            ))}
          </div>
        </CardContent>
      </Card>
    );
  }

  return (
    <Card>
      <CardContent className="p-6">
        <div className="flex items-center justify-between mb-4">
          <h2 className="text-lg font-semibold text-secondary-900">
            Notifications
          </h2>
          {unreadCount > 0 && (
            <span className="px-2 py-1 bg-error-100 text-error-700 rounded-full text-xs font-semibold">
              {unreadCount} new
            </span>
          )}
        </div>

        {notifications.length === 0 ? (
          <div className="text-center py-8 text-secondary-600">
            <svg className="mx-auto h-12 w-12 text-secondary-400" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M15 17h5l-1.405-1.405A2.032 2.032 0 0118 14.158V11a6.002 6.002 0 00-4-5.659V5a2 2 0 10-4 0v.341C7.67 6.165 6 8.388 6 11v3.159c0 .538-.214 1.055-.595 1.436L4 17h5m6 0v1a3 3 0 11-6 0v-1m6 0H9" />
            </svg>
            <p className="mt-2 text-sm">No notifications</p>
          </div>
        ) : (
          <div className="space-y-3">
            {notifications.map((notification) => (
              <div
                key={notification.id}
                className={`p-4 rounded-lg border ${
                  notification.read 
                    ? 'bg-white border-secondary-200' 
                    : 'bg-primary-50 border-primary-200'
                } cursor-pointer hover:shadow-sm transition-shadow`}
                onClick={() => !notification.read && handleMarkAsRead(notification.id)}
              >
                <div className="flex items-start justify-between">
                  <div className="flex-1">
                    <div className="flex items-center space-x-2 mb-1">
                      <span className={`px-2 py-0.5 rounded text-xs font-semibold ${
                        notification.priority === 'high' || notification.priority === 'urgent'
                          ? 'bg-error-100 text-error-700'
                          : notification.priority === 'medium'
                          ? 'bg-warning-100 text-warning-700'
                          : 'bg-secondary-100 text-secondary-700'
                      }`}>
                        {notification.priority}
                      </span>
                      <span className={`px-2 py-0.5 rounded text-xs ${
                        notification.type === 'alert'
                          ? 'bg-error-100 text-error-700'
                          : notification.type === 'warning'
                          ? 'bg-warning-100 text-warning-700'
                          : notification.type === 'success'
                          ? 'bg-success-100 text-success-700'
                          : 'bg-primary-100 text-primary-700'
                      }`}>
                        {notification.type}
                      </span>
                    </div>
                    <h4 className="font-semibold text-secondary-900">{notification.title}</h4>
                    <p className="text-sm text-secondary-600 mt-1">{notification.message}</p>
                    <p className="text-xs text-secondary-400 mt-2">
                      {new Date(notification.created_at).toLocaleString()}
                    </p>
                  </div>
                  {!notification.read && (
                    <div className="ml-4">
                      <div className="h-2 w-2 bg-primary-600 rounded-full"></div>
                    </div>
                  )}
                </div>
              </div>
            ))}
          </div>
        )}
      </CardContent>
    </Card>
  );
}

