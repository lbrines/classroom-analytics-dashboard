export type GoogleMode = 'GOOGLE' | 'MOCK';

export interface GoogleStatus {
  connected: boolean;
  mode: GoogleMode;
  email?: string;
  scopes?: string[];
}

export interface GoogleConnection {
  status: 'connected' | 'disconnected' | 'connecting' | 'error';
  email?: string;
  error?: string;
}

