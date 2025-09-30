export interface User {
  id: string;
  email: string;
  name: string;
  role: UserRole;
  active: boolean;
  created_at: string;
  updated_at: string;
}

export enum UserRole {
  ADMINISTRATOR = 'administrator',
  COORDINATOR = 'coordinator',
  TEACHER = 'teacher',
  STUDENT = 'student',
}

export interface LoginRequest {
  email: string;
  password: string;
}

export interface LoginResponse {
  access_token: string;
  token_type: string;
  expires_in: number;
  user: User;
}

export interface AuthState {
  user: User | null;
  token: string | null;
  isAuthenticated: boolean;
  isLoading: boolean;
  error: string | null;
}

export interface OAuthStatus {
  connected: boolean;
  provider: string | null;
  user_info: {
    email: string;
    name: string;
    picture: string;
  } | null;
}
