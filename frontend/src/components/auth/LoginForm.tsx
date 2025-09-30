import React, { useState } from 'react';
import { useForm } from 'react-hook-form';
import { zodResolver } from '@hookform/resolvers/zod';
import { z } from 'zod';
import { Button } from '@/components/ui/Button';
import { Input } from '@/components/ui/Input';
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from '@/components/ui/Card';
import { useAuth } from '@/hooks/useAuth';
import { useTranslation } from '@/hooks/useTranslation';
import { LoginRequest } from '@/types/auth.types';

const loginSchema = z.object({
  email: z.string().email('Please enter a valid email address'),
  password: z.string().min(1, 'Password is required'),
});

type LoginFormData = z.infer<typeof loginSchema>;

interface LoginFormProps {
  onSuccess?: () => void;
  onError?: (error: string) => void;
}

export function LoginForm({ onSuccess, onError }: LoginFormProps) {
  const { t } = useTranslation();
  const { login, isLoading, error } = useAuth();
  const [formError, setFormError] = useState<string | null>(null);

  const {
    register,
    handleSubmit,
    formState: { errors },
  } = useForm<LoginFormData>({
    resolver: zodResolver(loginSchema),
  });

  const onSubmit = async (data: LoginFormData) => {
    setFormError(null);
    
    try {
      await login(data as LoginRequest);
      onSuccess?.();
    } catch (err: any) {
      const errorMessage = err?.error?.message || t('auth.invalidCredentials');
      setFormError(errorMessage);
      onError?.(errorMessage);
    }
  };

  const displayError = formError || error;

  return (
    <Card className="w-full max-w-md mx-auto">
      <CardHeader className="text-center">
        <CardTitle className="text-2xl font-bold text-secondary-900">
          {t('auth.title')}
        </CardTitle>
        <CardDescription>
          {t('auth.subtitle')}
        </CardDescription>
      </CardHeader>
      <CardContent>
        <form onSubmit={handleSubmit(onSubmit)} className="space-y-4">
          {displayError && (
            <div className="rounded-md bg-error-50 p-4">
              <div className="text-sm text-error-700">{displayError}</div>
            </div>
          )}

          <Input
            {...register('email')}
            type="email"
            label={t('common.email')}
            placeholder={t('auth.emailPlaceholder')}
            error={errors.email?.message}
            disabled={isLoading}
          />

          <Input
            {...register('password')}
            type="password"
            label={t('common.password')}
            placeholder={t('auth.passwordPlaceholder')}
            error={errors.password?.message}
            disabled={isLoading}
          />

          <Button
            type="submit"
            className="w-full"
            isLoading={isLoading}
            disabled={isLoading}
          >
            {t('auth.loginButton')}
          </Button>
        </form>

        <div className="mt-6">
          <div className="relative">
            <div className="absolute inset-0 flex items-center">
              <div className="w-full border-t border-secondary-300" />
            </div>
            <div className="relative flex justify-center text-sm">
              <span className="bg-white px-2 text-secondary-500">Or continue with</span>
            </div>
          </div>

          <div className="mt-6">
            <OAuthButton />
          </div>
        </div>
      </CardContent>
    </Card>
  );
}

// Import OAuthButton component (we'll create it next)
import { OAuthButton } from './OAuthButton';
