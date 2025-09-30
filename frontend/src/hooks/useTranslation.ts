import { useTranslation as useI18nTranslation } from 'react-i18next';

export function useTranslation() {
  const { t, i18n } = useI18nTranslation();

  const changeLanguage = (language: string) => {
    i18n.changeLanguage(language);
  };

  const getCurrentLanguage = () => {
    return i18n.language;
  };

  const isLanguageSupported = (language: string) => {
    return i18n.hasResourceBundle(language, 'translation');
  };

  return {
    t,
    changeLanguage,
    getCurrentLanguage,
    isLanguageSupported,
    currentLanguage: i18n.language,
    isReady: i18n.isInitialized,
  };
}
