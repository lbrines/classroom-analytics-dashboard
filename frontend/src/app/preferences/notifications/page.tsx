'use client';

import { useState, useEffect } from 'react';
import { AuthGuard } from '@/components/auth/AuthGuard';
import { DashboardHeader } from '@/components/dashboard/DashboardHeader';
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/Card';
import { Button } from '@/components/ui/Button';
import { useAuth } from '@/hooks/useAuth';
import { useNotifications } from '@/hooks/useNotifications';

interface NotificationPreferences {
  channels: {
    inApp: boolean;
    email: boolean;
    telegram: boolean;
  };
  types: {
    assignment: boolean;
    studentRisk: boolean;
    announcement: boolean;
    grade: boolean;
    system: boolean;
  };
  schedule: {
    quietHoursEnabled: boolean;
    quietHoursStart: string;
    quietHoursEnd: string;
    digestEnabled: boolean;
    digestFrequency: 'daily' | 'weekly' | 'monthly';
    digestTime: string;
  };
}

export default function NotificationPreferencesPage() {
  const { user } = useAuth();
  const { preferences, updatePreferences, isLoading } = useNotifications();
  
  const [formData, setFormData] = useState<NotificationPreferences>({
    channels: {
      inApp: true,
      email: false,
      telegram: false,
    },
    types: {
      assignment: true,
      studentRisk: true,
      announcement: true,
      grade: false,
      system: true,
    },
    schedule: {
      quietHoursEnabled: false,
      quietHoursStart: '22:00',
      quietHoursEnd: '08:00',
      digestEnabled: false,
      digestFrequency: 'daily',
      digestTime: '18:00',
    },
  });

  const [isSaving, setIsSaving] = useState(false);
  const [saveStatus, setSaveStatus] = useState<'idle' | 'success' | 'error'>('idle');

  useEffect(() => {
    if (preferences) {
      setFormData(preferences);
    }
  }, [preferences]);

  const handleChannelChange = (channel: keyof NotificationPreferences['channels']) => {
    setFormData(prev => ({
      ...prev,
      channels: {
        ...prev.channels,
        [channel]: !prev.channels[channel],
      },
    }));
  };

  const handleTypeChange = (type: keyof NotificationPreferences['types']) => {
    setFormData(prev => ({
      ...prev,
      types: {
        ...prev.types,
        [type]: !prev.types[type],
      },
    }));
  };

  const handleScheduleChange = (field: string, value: any) => {
    setFormData(prev => ({
      ...prev,
      schedule: {
        ...prev.schedule,
        [field]: value,
      },
    }));
  };

  const handleSave = async () => {
    setIsSaving(true);
    setSaveStatus('idle');
    
    try {
      await updatePreferences(formData);
      setSaveStatus('success');
    } catch (error) {
      console.error('Failed to save preferences:', error);
      setSaveStatus('error');
    } finally {
      setIsSaving(false);
    }
  };

  const handleReset = () => {
    setFormData({
      channels: {
        inApp: true,
        email: false,
        telegram: false,
      },
      types: {
        assignment: true,
        studentRisk: true,
        announcement: true,
        grade: false,
        system: true,
      },
      schedule: {
        quietHoursEnabled: false,
        quietHoursStart: '22:00',
        quietHoursEnd: '08:00',
        digestEnabled: false,
        digestFrequency: 'daily',
        digestTime: '18:00',
      },
    });
  };

  return (
    <AuthGuard>
      <div className="min-h-screen bg-secondary-50">
        <DashboardHeader />
        
        <main className="py-6">
          <div className="mx-auto max-w-4xl px-4 sm:px-6 lg:px-8">
            <div className="mb-8">
              <h1 className="text-3xl font-bold text-secondary-900">
                Notification Preferences
              </h1>
              <p className="mt-2 text-sm text-secondary-600">
                Customize how and when you receive notifications
              </p>
            </div>

            <div className="space-y-6">
              {/* Channels */}
              <Card>
                <CardHeader>
                  <CardTitle>Notification Channels</CardTitle>
                </CardHeader>
                <CardContent>
                  <div className="space-y-4">
                    <div className="flex items-center justify-between">
                      <div>
                        <h3 className="text-sm font-medium text-secondary-900">In-App Notifications</h3>
                        <p className="text-sm text-secondary-600">Receive notifications within the application</p>
                      </div>
                      <label className="relative inline-flex items-center cursor-pointer">
                        <input
                          type="checkbox"
                          checked={formData.channels.inApp}
                          onChange={() => handleChannelChange('inApp')}
                          className="sr-only peer"
                        />
                        <div className="w-11 h-6 bg-secondary-200 peer-focus:outline-none peer-focus:ring-4 peer-focus:ring-primary-300 rounded-full peer peer-checked:after:translate-x-full peer-checked:after:border-white after:content-[''] after:absolute after:top-[2px] after:left-[2px] after:bg-white after:border-secondary-300 after:border after:rounded-full after:h-5 after:w-5 after:transition-all peer-checked:bg-primary-600"></div>
                      </label>
                    </div>

                    <div className="flex items-center justify-between">
                      <div>
                        <h3 className="text-sm font-medium text-secondary-900">Email Notifications</h3>
                        <p className="text-sm text-secondary-600">Receive notifications via email</p>
                      </div>
                      <label className="relative inline-flex items-center cursor-pointer">
                        <input
                          type="checkbox"
                          checked={formData.channels.email}
                          onChange={() => handleChannelChange('email')}
                          className="sr-only peer"
                        />
                        <div className="w-11 h-6 bg-secondary-200 peer-focus:outline-none peer-focus:ring-4 peer-focus:ring-primary-300 rounded-full peer peer-checked:after:translate-x-full peer-checked:after:border-white after:content-[''] after:absolute after:top-[2px] after:left-[2px] after:bg-white after:border-secondary-300 after:border after:rounded-full after:h-5 after:w-5 after:transition-all peer-checked:bg-primary-600"></div>
                      </label>
                    </div>

                    <div className="flex items-center justify-between">
                      <div>
                        <h3 className="text-sm font-medium text-secondary-900">Telegram Notifications</h3>
                        <p className="text-sm text-secondary-600">Receive notifications via Telegram</p>
                      </div>
                      <label className="relative inline-flex items-center cursor-pointer">
                        <input
                          type="checkbox"
                          checked={formData.channels.telegram}
                          onChange={() => handleChannelChange('telegram')}
                          className="sr-only peer"
                        />
                        <div className="w-11 h-6 bg-secondary-200 peer-focus:outline-none peer-focus:ring-4 peer-focus:ring-primary-300 rounded-full peer peer-checked:after:translate-x-full peer-checked:after:border-white after:content-[''] after:absolute after:top-[2px] after:left-[2px] after:bg-white after:border-secondary-300 after:border after:rounded-full after:h-5 after:w-5 after:transition-all peer-checked:bg-primary-600"></div>
                      </label>
                    </div>
                  </div>
                </CardContent>
              </Card>

              {/* Notification Types */}
              <Card>
                <CardHeader>
                  <CardTitle>Notification Types</CardTitle>
                </CardHeader>
                <CardContent>
                  <div className="space-y-4">
                    {[
                      { key: 'assignment', label: 'Assignment Updates', description: 'Deadlines, submissions, and grades' },
                      { key: 'studentRisk', label: 'Student Risk Alerts', description: 'Students at risk or falling behind' },
                      { key: 'announcement', label: 'Announcements', description: 'Course and system announcements' },
                      { key: 'grade', label: 'Grade Updates', description: 'New grades and feedback' },
                      { key: 'system', label: 'System Notifications', description: 'System updates and maintenance' },
                    ].map(({ key, label, description }) => (
                      <div key={key} className="flex items-center justify-between">
                        <div>
                          <h3 className="text-sm font-medium text-secondary-900">{label}</h3>
                          <p className="text-sm text-secondary-600">{description}</p>
                        </div>
                        <label className="relative inline-flex items-center cursor-pointer">
                          <input
                            type="checkbox"
                            checked={formData.types[key as keyof NotificationPreferences['types']]}
                            onChange={() => handleTypeChange(key as keyof NotificationPreferences['types'])}
                            className="sr-only peer"
                          />
                          <div className="w-11 h-6 bg-secondary-200 peer-focus:outline-none peer-focus:ring-4 peer-focus:ring-primary-300 rounded-full peer peer-checked:after:translate-x-full peer-checked:after:border-white after:content-[''] after:absolute after:top-[2px] after:left-[2px] after:bg-white after:border-secondary-300 after:border after:rounded-full after:h-5 after:w-5 after:transition-all peer-checked:bg-primary-600"></div>
                        </label>
                      </div>
                    ))}
                  </div>
                </CardContent>
              </Card>

              {/* Schedule */}
              <Card>
                <CardHeader>
                  <CardTitle>Schedule & Timing</CardTitle>
                </CardHeader>
                <CardContent>
                  <div className="space-y-6">
                    {/* Quiet Hours */}
                    <div>
                      <div className="flex items-center justify-between mb-4">
                        <div>
                          <h3 className="text-sm font-medium text-secondary-900">Quiet Hours</h3>
                          <p className="text-sm text-secondary-600">Pause notifications during specified hours</p>
                        </div>
                        <label className="relative inline-flex items-center cursor-pointer">
                          <input
                            type="checkbox"
                            checked={formData.schedule.quietHoursEnabled}
                            onChange={(e) => handleScheduleChange('quietHoursEnabled', e.target.checked)}
                            className="sr-only peer"
                          />
                          <div className="w-11 h-6 bg-secondary-200 peer-focus:outline-none peer-focus:ring-4 peer-focus:ring-primary-300 rounded-full peer peer-checked:after:translate-x-full peer-checked:after:border-white after:content-[''] after:absolute after:top-[2px] after:left-[2px] after:bg-white after:border-secondary-300 after:border after:rounded-full after:h-5 after:w-5 after:transition-all peer-checked:bg-primary-600"></div>
                        </label>
                      </div>
                      
                      {formData.schedule.quietHoursEnabled && (
                        <div className="grid grid-cols-2 gap-4">
                          <div>
                            <label className="block text-sm font-medium text-secondary-700 mb-1">
                              Start Time
                            </label>
                            <input
                              type="time"
                              value={formData.schedule.quietHoursStart}
                              onChange={(e) => handleScheduleChange('quietHoursStart', e.target.value)}
                              className="w-full px-3 py-2 border border-secondary-300 rounded-md focus:outline-none focus:ring-2 focus:ring-primary-500"
                            />
                          </div>
                          <div>
                            <label className="block text-sm font-medium text-secondary-700 mb-1">
                              End Time
                            </label>
                            <input
                              type="time"
                              value={formData.schedule.quietHoursEnd}
                              onChange={(e) => handleScheduleChange('quietHoursEnd', e.target.value)}
                              className="w-full px-3 py-2 border border-secondary-300 rounded-md focus:outline-none focus:ring-2 focus:ring-primary-500"
                            />
                          </div>
                        </div>
                      )}
                    </div>

                    {/* Digest */}
                    <div>
                      <div className="flex items-center justify-between mb-4">
                        <div>
                          <h3 className="text-sm font-medium text-secondary-900">Digest Notifications</h3>
                          <p className="text-sm text-secondary-600">Receive periodic summary notifications</p>
                        </div>
                        <label className="relative inline-flex items-center cursor-pointer">
                          <input
                            type="checkbox"
                            checked={formData.schedule.digestEnabled}
                            onChange={(e) => handleScheduleChange('digestEnabled', e.target.checked)}
                            className="sr-only peer"
                          />
                          <div className="w-11 h-6 bg-secondary-200 peer-focus:outline-none peer-focus:ring-4 peer-focus:ring-primary-300 rounded-full peer peer-checked:after:translate-x-full peer-checked:after:border-white after:content-[''] after:absolute after:top-[2px] after:left-[2px] after:bg-white after:border-secondary-300 after:border after:rounded-full after:h-5 after:w-5 after:transition-all peer-checked:bg-primary-600"></div>
                        </label>
                      </div>
                      
                      {formData.schedule.digestEnabled && (
                        <div className="grid grid-cols-2 gap-4">
                          <div>
                            <label className="block text-sm font-medium text-secondary-700 mb-1">
                              Frequency
                            </label>
                            <select
                              value={formData.schedule.digestFrequency}
                              onChange={(e) => handleScheduleChange('digestFrequency', e.target.value)}
                              className="w-full px-3 py-2 border border-secondary-300 rounded-md focus:outline-none focus:ring-2 focus:ring-primary-500"
                            >
                              <option value="daily">Daily</option>
                              <option value="weekly">Weekly</option>
                              <option value="monthly">Monthly</option>
                            </select>
                          </div>
                          <div>
                            <label className="block text-sm font-medium text-secondary-700 mb-1">
                              Time
                            </label>
                            <input
                              type="time"
                              value={formData.schedule.digestTime}
                              onChange={(e) => handleScheduleChange('digestTime', e.target.value)}
                              className="w-full px-3 py-2 border border-secondary-300 rounded-md focus:outline-none focus:ring-2 focus:ring-primary-500"
                            />
                          </div>
                        </div>
                      )}
                    </div>
                  </div>
                </CardContent>
              </Card>

              {/* Actions */}
              <Card>
                <CardContent className="pt-6">
                  <div className="flex items-center justify-between">
                    <div className="flex space-x-3">
                      <Button
                        onClick={handleSave}
                        disabled={isSaving || isLoading}
                        className="bg-primary-600 hover:bg-primary-700"
                      >
                        {isSaving ? 'Saving...' : 'Save Preferences'}
                      </Button>
                      <Button
                        onClick={handleReset}
                        variant="outline"
                        disabled={isSaving || isLoading}
                      >
                        Reset to Defaults
                      </Button>
                    </div>
                    
                    {saveStatus === 'success' && (
                      <div className="text-sm text-success-600">
                        ✓ Preferences saved successfully
                      </div>
                    )}
                    {saveStatus === 'error' && (
                      <div className="text-sm text-error-600">
                        ✗ Failed to save preferences
                      </div>
                    )}
                  </div>
                </CardContent>
              </Card>
            </div>
          </div>
        </main>
      </div>
    </AuthGuard>
  );
}

