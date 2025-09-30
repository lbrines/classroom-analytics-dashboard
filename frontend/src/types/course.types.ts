export type CourseState = 'ACTIVE' | 'ARCHIVED' | 'PROVISIONED' | 'DECLINED';

export interface Course {
  id: string;
  name: string;
  section?: string;
  description?: string;
  room?: string;
  owner_id: string;
  enrollment_code?: string;
  course_state: CourseState;
  creation_time: string;
  update_time: string;
  alternate_link?: string;
  teacher_group_email?: string;
  course_group_email?: string;
  guardians_enabled: boolean;
  calendar_id?: string;
}

export interface Student {
  user_id: string;
  full_name: string;
  email_address?: string;
  course_id: string;
  profile_id?: string;
  photo_url?: string;
}

export interface StudentProgress {
  student_id: string;
  student_name: string;
  course_id: string;
  course_name: string;
  progress: number; // 0-100
  grade?: number;
  assignments_completed: number;
  assignments_total: number;
  last_activity?: string;
}

