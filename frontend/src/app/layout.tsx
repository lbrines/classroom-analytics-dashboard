import type { Metadata } from 'next';
import { Inter } from 'next/font/google';
import './globals.css';
import { AuthProvider } from '@/components/auth/AuthProvider';
import { QueryProvider } from '@/components/providers/QueryProvider';

const inter = Inter({ subsets: ['latin'] });

export const metadata: Metadata = {
  title: 'Educational Dashboard',
  description: 'Educational Dashboard - Stage 1 Implementation',
  keywords: ['education', 'dashboard', 'learning', 'management'],
  authors: [{ name: 'Educational Dashboard Team' }],
  // Disable browser autofill to prevent extension overlay errors
  other: {
    'x-autofill': 'off',
  },
};

export const viewport = {
  width: 'device-width',
  initialScale: 1,
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <head>
        <link rel="icon" href="/favicon.ico" />
        {/* Prevent browser extension autofill overlays */}
        <meta name="autocomplete" content="off" />
      </head>
      <body className={inter.className} data-autofill="off">
        <QueryProvider>
          <AuthProvider>
            {children}
          </AuthProvider>
        </QueryProvider>
      </body>
    </html>
  );
}
