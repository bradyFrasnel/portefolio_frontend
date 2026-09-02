import { createI18n } from 'vue-i18n'
import en from './locales/en.json'
import fr from './locales/fr.json'

const messages = {
  en,
  fr
}

const i18n = createI18n({
  locale: 'fr',
  fallbackLocale: 'en',
  messages,
  legacy: false
})

export default i18n
