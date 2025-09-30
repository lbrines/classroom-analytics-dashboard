export interface OAuthURLRequest {
  provider: string;
  redirect_uri?: string;
}

export interface OAuthURLResponse {
  auth_url: string;
  state: string;
}

export interface OAuthCallbackRequest {
  code: string;
  state: string;
  provider: string;
}

export interface OAuthCallbackResponse {
  access_token: string;
  token_type: string;
  expires_in: number;
  user: {
    id: string;
    email: string;
    name: string;
    role: string;
    active: boolean;
  };
}

export interface OAuthRevokeRequest {
  provider: string;
}

export interface OAuthRevokeResponse {
  message: string;
}

export interface OAuthStatusResponse {
  connected: boolean;
  provider: string | null;
  user_info: {
    email: string;
    name: string;
    picture: string;
  } | null;
}
