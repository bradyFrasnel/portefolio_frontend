<template>
  <div class="min-h-screen bg-obsidian text-off-white">
    <header class="bg-dark-jungle border-b border-gray-800">
      <nav class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="flex justify-between items-center h-16">
          <div class="text-2xl font-bold text-emerald">Mon Portfolio</div>
          <div class="hidden md:flex space-x-8">
            <router-link to="/" class="text-gray-custom hover:text-emerald transition-colors">Accueil</router-link>
            <router-link to="/portfolio" class="text-gray-custom hover:text-emerald transition-colors">Portfolio</router-link>
            <router-link to="/services" class="text-gray-custom hover:text-emerald transition-colors">Services</router-link>
            <router-link to="/contact" class="text-gray-custom hover:text-emerald transition-colors">Contact</router-link>
            <router-link to="/admin" class="text-gray-custom hover:text-emerald transition-colors">Admin</router-link>
          </div>
          <div class="flex items-center space-x-4">
            <button 
              @click="toggleDarkMode" 
              class="p-2 rounded-lg bg-gray-800 hover:bg-gray-700 transition-colors"
            >
              {{ isDarkMode ? '🌙' : '☀️' }}
            </button>
            <button 
              @click="toggleMobileMenu" 
              class="md:hidden p-2 rounded-lg bg-gray-800 hover:bg-gray-700 transition-colors"
            >
              {{ mobileMenuOpen ? '✕' : '☰' }}
            </button>
          </div>
        </div>
        <div v-if="mobileMenuOpen" class="md:hidden py-4 border-t border-gray-800">
          <div class="flex flex-col space-y-2">
            <router-link to="/" class="text-gray-custom hover:text-emerald transition-colors py-2">Accueil</router-link>
            <router-link to="/portfolio" class="text-gray-custom hover:text-emerald transition-colors py-2">Portfolio</router-link>
            <router-link to="/services" class="text-gray-custom hover:text-emerald transition-colors py-2">Services</router-link>
            <router-link to="/contact" class="text-gray-custom hover:text-emerald transition-colors py-2">Contact</router-link>
          </div>
        </div>
      </nav>
    </header>

    <main class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12">
      <section class="text-center mb-16">
        <h1 class="text-4xl md:text-5xl font-bold text-off-white mb-6">
          Services pour PME
        </h1>
        <p class="text-xl text-gray-custom max-w-3xl mx-auto">
          Des solutions web sur mesure pour aider votre entreprise à se développer et à prospérer dans l'ère numérique
        </p>
      </section>

      <div v-if="true" class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6 sm:gap-8 mb-16">
        <div class="bg-dark-jungle p-6 sm:p-8 rounded-xl border border-gray-800 hover:border-emerald transition-all" data-aos="fade-up" data-aos-delay="100">
          <div class="text-emerald text-3xl sm:text-4xl mb-6">🌐</div>
          <h3 class="text-xl sm:text-2xl font-semibold mb-4 text-off-white">Développement Web</h3>
          <p class="text-gray-custom mb-6 text-sm sm:text-base">
            Sites vitrines modernes, applications web complexes, plateformes e-commerce. 
            Des solutions adaptées à vos besoins métier.
          </p>
          <ul class="space-y-2 text-gray-custom text-sm sm:text-base">
            <li class="flex items-start">
              <span class="text-emerald mr-2">✓</span>
              <span class="hidden sm:inline">Sites vitrines responsives</span>
              <span class="sm:hidden">Sites responsives</span>
            </li>
            <li class="flex items-start">
              <span class="text-emerald mr-2">✓</span>
              <span class="hidden sm:inline">Applications Django sur mesure</span>
              <span class="sm:hidden">Apps Django</span>
            </li>
            <li class="flex items-start">
              <span class="text-emerald mr-2">✓</span>
              <span class="hidden sm:inline">Plateformes e-commerce</span>
              <span class="sm:hidden">E-commerce</span>
            </li>
          </ul>
        </div>

        <div class="bg-dark-jungle p-6 sm:p-8 rounded-xl border border-gray-800 hover:border-emerald transition-all" data-aos="fade-up" data-aos-delay="200">
          <div class="text-emerald text-3xl sm:text-4xl mb-6">🤖</div>
          <h3 class="text-xl sm:text-2xl font-semibold mb-4 text-off-white">Automatisation</h3>
          <p class="text-gray-custom mb-6 text-sm sm:text-base">
            Scripts Python pour automatiser vos tâches répétitives, web scraping, 
            traitement et analyse de données.
          </p>
          <ul class="space-y-2 text-gray-custom text-sm sm:text-base">
            <li class="flex items-start">
              <span class="text-emerald mr-2">✓</span>
              <span class="hidden sm:inline">Web scraping et extraction</span>
              <span class="sm:hidden">Web scraping</span>
            </li>
            <li class="flex items-start">
              <span class="text-emerald mr-2">✓</span>
              <span class="hidden sm:inline">Automatisation de processus</span>
              <span class="sm:hidden">Automatisation</span>
            </li>
            <li class="flex items-start">
              <span class="text-emerald mr-2">✓</span>
              <span class="hidden sm:inline">Traitement de données</span>
              <span class="sm:hidden">Traitement données</span>
            </li>
          </ul>
        </div>

        <div class="bg-dark-jungle p-6 sm:p-8 rounded-xl border border-gray-800 hover:border-emerald transition-all" data-aos="fade-up" data-aos-delay="300">
          <div class="text-emerald text-3xl sm:text-4xl mb-6">🔧</div>
          <h3 class="text-xl sm:text-2xl font-semibold mb-4 text-off-white">Maintenance</h3>
          <p class="text-gray-custom mb-6 text-sm sm:text-base">
            Audit de code, correction de bugs, mises à jour de sécurité, 
            optimisation des performances.
          </p>
          <ul class="space-y-2 text-gray-custom text-sm sm:text-base">
            <li class="flex items-start">
              <span class="text-emerald mr-2">✓</span>
              <span class="hidden sm:inline">Audit et optimisation</span>
              <span class="sm:hidden">Audit optimisation</span>
            </li>
            <li class="flex items-start">
              <span class="text-emerald mr-2">✓</span>
              <span class="hidden sm:inline">Correction de bugs</span>
              <span class="sm:hidden">Correction bugs</span>
            </li>
            <li class="flex items-start">
              <span class="text-emerald mr-2">✓</span>
              <span class="hidden sm:inline">Mises à jour et sécurité</span>
              <span class="sm:hidden">Màj sécurité</span>
            </li>
          </ul>
        </div>
      </div>

      <section class="mb-16">
        <h2 class="text-3xl font-bold text-center text-off-white mb-12">Ma Méthodologie</h2>
        <div class="grid md:grid-cols-4 gap-8">
          <div class="text-center">
            <div class="w-16 h-16 bg-emerald text-obsidian rounded-full flex items-center justify-center mx-auto mb-4 text-2xl font-bold">
              1
            </div>
            <h3 class="text-xl font-semibold mb-2 text-off-white">Analyse</h3>
            <p class="text-gray-custom">Compréhension de vos besoins et objectifs métier</p>
          </div>
          <div class="text-center">
            <div class="w-16 h-16 bg-emerald text-obsidian rounded-full flex items-center justify-center mx-auto mb-4 text-2xl font-bold">
              2
            </div>
            <h3 class="text-xl font-semibold mb-2 text-off-white">Conception</h3>
            <p class="text-gray-custom">Design UX/UI et architecture technique</p>
          </div>
          <div class="text-center">
            <div class="w-16 h-16 bg-emerald text-obsidian rounded-full flex items-center justify-center mx-auto mb-4 text-2xl font-bold">
              3
            </div>
            <h3 class="text-xl font-semibold mb-2 text-off-white">Développement</h3>
            <p class="text-gray-custom">Codage agile avec tests réguliers</p>
          </div>
          <div class="text-center">
            <div class="w-16 h-16 bg-emerald text-obsidian rounded-full flex items-center justify-center mx-auto mb-4 text-2xl font-bold">
              4
            </div>
            <h3 class="text-xl font-semibold mb-2 text-off-white">Livraison</h3>
            <p class="text-gray-custom">Déploiement et formation utilisateur</p>
          </div>
        </div>
      </section>

      <section class="text-center">
        <h2 class="text-3xl font-bold text-off-white mb-8">Tarification Indicative</h2>
        <div class="grid md:grid-cols-3 gap-8 max-w-5xl mx-auto">
          <div class="bg-dark-jungle p-8 rounded-xl border border-gray-800">
            <h3 class="text-xl font-semibold mb-4 text-emerald">Site Vitrine</h3>
            <div class="text-3xl font-bold text-off-white mb-4">À partir de 1500€</div>
            <p class="text-gray-custom mb-6">Site web professionnel 5-8 pages</p>
            <ul class="space-y-2 text-gray-custom text-sm">
              <li>• Design responsive</li>
              <li>• Formulaire de contact</li>
              <li>• Référencement de base</li>
              <li>• Formation incluse</li>
            </ul>
          </div>
          <div class="bg-dark-jungle p-8 rounded-xl border border-emerald">
            <h3 class="text-xl font-semibold mb-4 text-emerald">Application Web</h3>
            <div class="text-3xl font-bold text-off-white mb-4">À partir de 3000€</div>
            <p class="text-gray-custom mb-6">Application avec fonctionnalités avancées</p>
            <ul class="space-y-2 text-gray-custom text-sm">
              <li>• Base de données</li>
              <li>• Interface admin</li>
              <li>• API REST</li>
              <li>• Maintenance 3 mois</li>
            </ul>
          </div>
          <div class="bg-dark-jungle p-8 rounded-xl border border-gray-800">
            <h3 class="text-xl font-semibold mb-4 text-emerald">Sur Mesure</h3>
            <div class="text-3xl font-bold text-off-white mb-4">Sur devis</div>
            <p class="text-gray-custom mb-6">Projets complexes et spécifiques</p>
            <ul class="space-y-2 text-gray-custom text-sm">
              <li>• Audit personnalisé</li>
              <li>• Architecture sur mesure</li>
              <li>• Scalabilité garantie</li>
              <li>• Support prioritaire</li>
            </ul>
          </div>
        </div>
        <div class="mt-12">
          <router-link 
            to="/contact" 
            class="bg-emerald text-obsidian px-8 py-3 rounded-lg hover:bg-neon-lime transition-all transform hover:scale-105 font-semibold"
          >
            Demander un devis gratuit
          </router-link>
        </div>
      </section>
    </main>
    
    <!-- Footer -->
    <Footer />
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import Footer from '../components/Footer.vue'

const isDarkMode = ref(true)
const mobileMenuOpen = ref(false)

const toggleDarkMode = () => {
  isDarkMode.value = !isDarkMode.value
  document.documentElement.classList.toggle('dark')
}

const toggleMobileMenu = () => {
  mobileMenuOpen.value = !mobileMenuOpen.value
}

onMounted(() => {
  document.documentElement.classList.add('dark')
})
</script>
