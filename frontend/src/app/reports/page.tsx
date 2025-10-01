'use client';

import { useState } from 'react';
import { AuthGuard } from '@/components/auth/AuthGuard';
import { DashboardHeader } from '@/components/dashboard/DashboardHeader';
import { Card, CardContent } from '@/components/ui/Card';
import { Button } from '@/components/ui/Button';

export default function ReportsPage() {
  const [generating, setGenerating] = useState(false);

  const handleGenerateReport = async (reportType: string) => {
    setGenerating(true);
    // TODO: Integrate with API
    setTimeout(() => setGenerating(false), 2000);
  };

  const reportTypes = [
    {
      id: 'course_performance',
      name: 'Course Performance',
      description: 'Detailed metrics and analytics for course performance',
      icon: '📚',
    },
    {
      id: 'student_progress',
      name: 'Student Progress',
      description: 'Individual student progress and achievements',
      icon: '🎓',
    },
    {
      id: 'engagement',
      name: 'Engagement Report',
      description: 'Student engagement and participation metrics',
      icon: '📈',
    },
    {
      id: 'completion_rates',
      name: 'Completion Rates',
      description: 'Assignment and course completion statistics',
      icon: '✅',
    },
  ];

  return (
    <AuthGuard>
      <div className="min-h-screen bg-secondary-50">
        <DashboardHeader />
        
        <main className="py-6">
          <div className="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
            <div className="mb-8">
              <h1 className="text-3xl font-bold text-secondary-900">
                Reports
              </h1>
              <p className="mt-2 text-sm text-secondary-600">
                Generate and export detailed reports
              </p>
            </div>

            <div className="grid grid-cols-1 gap-6 md:grid-cols-2 lg:grid-cols-4">
              {reportTypes.map((reportType) => (
                <Card key={reportType.id} className="hover:shadow-lg transition-shadow">
                  <CardContent className="p-6">
                    <div className="text-center">
                      <div className="text-5xl mb-4">{reportType.icon}</div>
                      <h3 className="text-lg font-semibold text-secondary-900 mb-2">
                        {reportType.name}
                      </h3>
                      <p className="text-sm text-secondary-600 mb-4">
                        {reportType.description}
                      </p>
                      <Button
                        onClick={() => handleGenerateReport(reportType.id)}
                        disabled={generating}
                        className="w-full"
                      >
                        {generating ? 'Generating...' : 'Generate'}
                      </Button>
                    </div>
                  </CardContent>
                </Card>
              ))}
            </div>

            <div className="mt-8">
              <Card>
                <CardContent className="p-6">
                  <h3 className="text-lg font-semibold text-secondary-900 mb-4">
                    Recent Reports
                  </h3>
                  <div className="text-center py-8 text-secondary-600">
                    <svg className="mx-auto h-12 w-12 text-secondary-400" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                      <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" />
                    </svg>
                    <p className="mt-2 text-sm">No reports generated yet</p>
                    <p className="text-xs text-secondary-500 mt-1">
                      Generate your first report using the options above
                    </p>
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

