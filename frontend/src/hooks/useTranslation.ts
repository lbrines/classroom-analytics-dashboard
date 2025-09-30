'use client';

import { useTranslation as useI18nTranslation } from 'react-i18next';
import { useEffect } from 'react';
import '@/i18n/config';

export function useTranslation() {
  // Initialize i18n on client side only
  useEffect(() => {
    // i18n is initialized in the imported config
  }, []);

  try {
    const { t, i18n } = useI18nTranslation();

    const changeLanguage = (language: string) => {
      if (i18n && i18n.changeLanguage) {
        i18n.changeLanguage(language);
      }
    };

    const getCurrentLanguage = () => {
      return i18n?.language || 'en';
    };

    const isLanguageSupported = (language: string) => {
      return i18n?.hasResourceBundle ? i18n.hasResourceBundle(language, 'translation') : false;
    };

    return {
      t: t || ((key: string) => key), // Fallback to key if translation fails
      changeLanguage,
      getCurrentLanguage,
      isLanguageSupported,
      currentLanguage: i18n?.language || 'en',
      isReady: i18n?.isInitialized || false,
    };
  } catch (error) {
    // Fallback when i18next is not available
    console.warn('i18next not available, using fallback translations');
    return {
      t: (key: string) => key,
      changeLanguage: () => {},
      getCurrentLanguage: () => 'en',
      isLanguageSupported: () => false,
      currentLanguage: 'en',
      isReady: false,
    };
  }
}
