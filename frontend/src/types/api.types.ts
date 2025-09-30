export interface ApiResponse<T = any> {
  data: T;
  meta: {
    timestamp: string;
    version: string;
    request_id: string;
  };
}

export interface ApiError {
  error: {
    code: string;
    message: string;
    details?: Record<string, any>;
  };
  meta: {
    timestamp: string;
    version: string;
    request_id: string;
  };
}

export interface HealthResponse {
  status: string;
  timestamp: number;
  version: string;
  environment: string;
  uptime: number;
}

export interface PaginationMeta {
  page: number;
  size: number;
  total: number;
  total_pages: number;
}

export interface PaginatedResponse<T> {
  data: T[];
  meta: PaginationMeta;
}
