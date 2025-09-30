export const OAUTH_PROVIDERS = {
  GOOGLE: 'google',
} as const;

export const OAUTH_SCOPES = {
  GOOGLE: [
    'https://www.googleapis.com/auth/userinfo.email',
    'https://www.googleapis.com/auth/userinfo.profile',
    'https://www.googleapis.com/auth/classroom.courses.readonly',
  ],
} as const;

export const OAUTH_STATE_KEY = 'oauth_state';
export const OAUTH_REDIRECT_KEY = 'oauth_redirect';

export const OAUTH_CALLBACK_URL = '/oauth/callback';
