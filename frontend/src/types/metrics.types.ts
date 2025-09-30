export interface CourseMetrics {
  course_id: string;
  course_name: string;
  total_students: number;
  active_students: number;
  completion_rate: number;
  average_grade: number;
  assignments_total: number;
  assignments_completed: number;
  engagement_score: number;
}

export interface StudentMetrics {
  student_id: string;
  student_name: string;
  courses_enrolled: number;
  courses_completed: number;
  overall_progress: number;
  average_grade: number;
  assignments_completed: number;
  assignments_pending: number;
  streak_days: number;
}

export interface DashboardMetrics {
  role: string;
  user_id: string;
  overview: Record<string, any>;
  metrics: Record<string, any>;
  trends?: Record<string, any>;
}

export interface ChartData {
  labels: string[];
  series: number[] | number[][];
  colors?: string[];
}

