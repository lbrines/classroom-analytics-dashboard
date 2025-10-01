'use client';

import { useTranslation as useI18nTranslation } from 'react-i18next';
import { useEffect } from 'react';
import '@/i18n/config';

export function useTranslation() {
  // Initialize i18n on client side only
  useEffect(() => {
    // i18n is initialized in the imported config
  }, []);

  // Always call the hook, but handle errors gracefully
  const translationResult = useI18nTranslation();
  
  const changeLanguage = (language: string) => {
    if (translationResult.i18n && translationResult.i18n.changeLanguage) {
      translationResult.i18n.changeLanguage(language);
    }
  };

  const getCurrentLanguage = () => {
    return translationResult.i18n?.language || 'en';
  };

  const isLanguageSupported = (language: string) => {
    return translationResult.i18n?.hasResourceBundle ? translationResult.i18n.hasResourceBundle(language, 'translation') : false;
  };

  return {
    t: translationResult.t || ((key: string) => key), // Fallback to key if translation fails
    changeLanguage,
    getCurrentLanguage,
    isLanguageSupported,
    currentLanguage: translationResult.i18n?.language || 'en',
    isReady: translationResult.i18n?.isInitialized || false,
  };
}
