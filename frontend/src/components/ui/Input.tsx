import React from 'react';
import { cn } from '@/lib/utils';

export interface InputProps extends React.InputHTMLAttributes<HTMLInputElement> {
  label?: string;
  error?: string;
  helperText?: string;
}

const Input = React.forwardRef<HTMLInputElement, InputProps>(
  ({ className, type = 'text', label, error, helperText, id, ...props }, ref) => {
    const inputId = id || `input-${Math.random().toString(36).substr(2, 9)}`;

    return (
      <div className="space-y-1">
        {label && (
          <label
            htmlFor={inputId}
            className="block text-sm font-medium text-secondary-700"
          >
            {label}
          </label>
        )}
        <input
          type={type}
          className={cn(
            'block w-full rounded-md border border-secondary-300 px-3 py-2 text-sm placeholder:text-secondary-400 focus:border-primary-500 focus:outline-none focus:ring-1 focus:ring-primary-500 disabled:cursor-not-allowed disabled:bg-secondary-50 disabled:text-secondary-500',
            error && 'border-error-300 focus:border-error-500 focus:ring-error-500',
            className
          )}
          ref={ref}
          id={inputId}
          {...props}
        />
        {error && (
          <p className="text-sm text-error-600">{error}</p>
        )}
        {helperText && !error && (
          <p className="text-sm text-secondary-500">{helperText}</p>
        )}
      </div>
    );
  }
);

Input.displayName = 'Input';

export { Input };
