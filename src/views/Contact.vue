<template>
  <div class="min-h-screen bg-gradient-to-br from-blue-50 to-indigo-100">
    <header class="bg-white shadow-sm">
      <nav class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="flex justify-between items-center h-16">
          <div class="text-2xl font-bold text-indigo-600">Mon Portfolio</div>
          <div class="flex space-x-8">
            <router-link to="/" class="text-gray-700 hover:text-indigo-600">Accueil</router-link>
            <router-link to="/portfolio" class="text-gray-700 hover:text-indigo-600">Portfolio</router-link>
            <router-link to="/contact" class="text-gray-700 hover:text-indigo-600">Contact</router-link>
          </div>
        </div>
      </nav>
    </header>

    <main class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12">
      <section class="text-center mb-12">
        <h1 class="text-4xl md:text-5xl font-bold text-gray-900 mb-4">
          Contactez-moi
        </h1>
        <p class="text-xl text-gray-600 max-w-3xl mx-auto">
          N'hésitez pas à me contacter pour discuter de vos projets ou pour toute collaboration
        </p>
      </section>

      <div class="grid md:grid-cols-2 gap-12">
        <div>
          <div class="bg-white rounded-xl shadow-lg p-8">
            <h2 class="text-2xl font-semibold mb-6">Envoyez un message</h2>
            
            <form @submit.prevent="submitForm" class="space-y-6">
              <div>
                <label for="name" class="block text-sm font-medium text-gray-700 mb-2">
                  Nom complet
                </label>
                <input
                  type="text"
                  id="name"
                  v-model="form.nom"
                  required
                  class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500 outline-none transition-colors"
                  placeholder="Votre nom"
                />
              </div>

              <div>
                <label for="email" class="block text-sm font-medium text-gray-700 mb-2">
                  Email
                </label>
                <input
                  type="email"
                  id="email"
                  v-model="form.email"
                  required
                  class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500 outline-none transition-colors"
                  placeholder="votre@email.com"
                />
              </div>

              <div>
                <label for="subject" class="block text-sm font-medium text-gray-700 mb-2">
                  Sujet / Type de projet
                </label>
                <input
                  type="text"
                  id="subject"
                  v-model="form.type_projet"
                  required
                  class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500 outline-none transition-colors"
                  placeholder="Sujet du message"
                />
              </div>

              <div>
                <label for="message" class="block text-sm font-medium text-gray-700 mb-2">
                  Message
                </label>
                <textarea
                  id="message"
                  v-model="form.message"
                  required
                  rows="5"
                  class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500 outline-none transition-colors resize-none"
                  placeholder="Votre message..."
                ></textarea>
              </div>

              <button
                type="submit"
                :disabled="sending"
                class="w-full bg-indigo-600 text-white py-3 rounded-lg hover:bg-indigo-700 transition-colors disabled:bg-gray-400 disabled:cursor-not-allowed"
              >
                {{ sending ? 'Envoi en cours...' : 'Envoyer le message' }}
              </button>
            </form>

            <div v-if="successMessage" class="mt-4 p-4 bg-green-100 border border-green-400 text-green-700 rounded-lg">
              {{ successMessage }}
            </div>

            <div v-if="errorMessage" class="mt-4 p-4 bg-red-100 border border-red-400 text-red-700 rounded-lg">
              {{ errorMessage }}
            </div>
          </div>
        </div>

        <div class="space-y-8">
          <div class="bg-white rounded-xl shadow-lg p-8">
            <h2 class="text-2xl font-semibold mb-6">Informations de contact</h2>
            
            <div class="space-y-4">
              <div class="flex items-center space-x-4">
                <div class="text-indigo-600 text-2xl">📧</div>
                <div>
                  <p class="font-medium">Email</p>
                  <p class="text-gray-600">mokumabrady13@gmail.com</p>
                </div>
              </div>

              <div class="flex items-center space-x-4">
                <div class="text-indigo-600 text-2xl">📱</div>
                <div>
                  <p class="font-medium">Téléphone</p>
                  <p class="text-gray-600">074 14 59 49 / 062 44 50 33</p>
                </div>
              </div>

              <div class="flex items-center space-x-4">
                <div class="text-indigo-600 text-2xl">📍</div>
                <div>
                  <p class="font-medium">Localisation</p>
                  <p class="text-gray-600">Libreville/Gabon</p>
                </div>
              </div>
            </div>
          </div>

          <div class="bg-white rounded-xl shadow-lg p-8">
            <h2 class="text-2xl font-semibold mb-6">Réseaux sociaux</h2>
            
            <div class="flex space-x-4">
              <a 
                href="https://github.com" 
                target="_blank"
                class="w-12 h-12 bg-gray-800 text-white rounded-lg flex items-center justify-center hover:bg-gray-700 transition-colors"
              >
                <span class="text-xl">🐙</span>
              </a>
              <a 
                href="https://linkedin.com" 
                target="_blank"
                class="w-12 h-12 bg-blue-600 text-white rounded-lg flex items-center justify-center hover:bg-blue-700 transition-colors"
              >
                <span class="text-xl">💼</span>
              </a>
              <a 
                href="https://twitter.com" 
                target="_blank"
                class="w-12 h-12 bg-sky-500 text-white rounded-lg flex items-center justify-center hover:bg-sky-600 transition-colors"
              >
                <span class="text-xl">🐙</span>
              </a>
            </div>
          </div>
        </div>
      </div>
    </main>
    
    <!-- Footer -->
    <Footer />
  </div>
</template>

<script setup>
import { ref } from 'vue'
import api from '../services/api.js'
import Footer from '../components/Footer.vue'

const form = ref({
  nom: '',
  email: '',
  type_projet: '',
  message: ''
})

const sending = ref(false)
const successMessage = ref('')
const errorMessage = ref('')

const submitForm = async () => {
  sending.value = true
  successMessage.value = ''
  errorMessage.value = ''

  try {
    await api.sendContact(form.value)
    successMessage.value = 'Message envoyé avec succès ! Je vous répondrai dans les plus brefs délais.'
    
    // Réinitialiser le formulaire
    form.value = {
      name: '',
      email: '',
      subject: '',
      message: ''
    }
  } catch (error) {
    console.error('Erreur:', error)
    errorMessage.value = 'Une erreur est survenue. Veuillez réessayer plus tard ou me contacter directement par email.'
  } finally {
    sending.value = false
  }
}
</script>
