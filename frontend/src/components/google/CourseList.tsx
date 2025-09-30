'use client';

import React from 'react';
import { Card, CardContent } from '@/components/ui/Card';
import { useCourses } from '@/hooks/useCourses';
import { Course } from '@/types/course.types';

export function CourseList() {
  const { courses, isLoading, error } = useCourses();

  if (isLoading) {
    return (
      <div className="space-y-4">
        {[1, 2, 3].map(i => (
          <Card key={i} className="animate-pulse">
            <CardContent className="p-6">
              <div className="h-16 bg-secondary-100 rounded"></div>
            </CardContent>
          </Card>
        ))}
      </div>
    );
  }

  if (error) {
    return (
      <Card>
        <CardContent className="p-6">
          <div className="text-center text-error-600">
            <p>Failed to load courses</p>
          </div>
        </CardContent>
      </Card>
    );
  }

  if (courses.length === 0) {
    return (
      <Card>
        <CardContent className="p-6">
          <div className="text-center text-secondary-600">
            <p>No courses available</p>
          </div>
        </CardContent>
      </Card>
    );
  }

  return (
    <div className="space-y-4">
      {courses.map((course: Course) => (
        <Card key={course.id} className="hover:shadow-md transition-shadow cursor-pointer">
          <CardContent className="p-6">
            <div className="flex items-start justify-between">
              <div className="flex-1">
                <h3 className="text-lg font-semibold text-secondary-900">
                  {course.name}
                </h3>
                {course.section && (
                  <p className="text-sm text-secondary-600 mt-1">
                    {course.section}
                  </p>
                )}
                {course.description && (
                  <p className="text-sm text-secondary-500 mt-2 line-clamp-2">
                    {course.description}
                  </p>
                )}
                {course.room && (
                  <p className="text-xs text-secondary-400 mt-2">
                    📍 {course.room}
                  </p>
                )}
              </div>
              <div className="ml-4">
                <span className={`
                  px-3 py-1 rounded-full text-xs font-medium
                  ${course.course_state === 'ACTIVE' 
                    ? 'bg-success-100 text-success-700' 
                    : 'bg-secondary-100 text-secondary-700'}
                `}>
                  {course.course_state}
                </span>
              </div>
            </div>
            
            {course.enrollment_code && (
              <div className="mt-4 pt-4 border-t border-secondary-100">
                <p className="text-xs text-secondary-600">
                  Enrollment Code: <span className="font-mono font-semibold">{course.enrollment_code}</span>
                </p>
              </div>
            )}
          </CardContent>
        </Card>
      ))}
    </div>
  );
}

