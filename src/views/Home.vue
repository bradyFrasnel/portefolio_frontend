<template>
  <div class="min-h-screen bg-obsidian text-off-white">
    <!-- Navigation -->
    <header class="fixed top-0 w-full bg-dark-jungle/95 backdrop-blur-sm border-b border-gray-800 z-50">
      <nav class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="flex justify-between items-center h-16">
          <div class="text-2xl font-bold text-emerald">Brady Portfolio</div>
          <div class="hidden md:flex space-x-8">
            <button @click="scrollToSection('hero')" class="text-gray-custom hover:text-emerald transition-colors">Accueil</button>
            <button @click="scrollToSection('portfolio')" class="text-gray-custom hover:text-emerald transition-colors">Portfolio</button>
            <button @click="scrollToSection('services')" class="text-gray-custom hover:text-emerald transition-colors">Services</button>
            <button @click="scrollToSection('contact')" class="text-gray-custom hover:text-emerald transition-colors">Contact</button>
            <button @click="scrollToSection('identifiants')" class="text-gray-custom hover:text-emerald transition-colors">Identifiants</button>
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
            <button @click="scrollToSection('hero')" class="text-gray-custom hover:text-emerald transition-colors py-2">Accueil</button>
            <button @click="scrollToSection('portfolio')" class="text-gray-custom hover:text-emerald transition-colors py-2">Portfolio</button>
            <button @click="scrollToSection('services')" class="text-gray-custom hover:text-emerald transition-colors py-2">Services</button>
            <button @click="scrollToSection('contact')" class="text-gray-custom hover:text-emerald transition-colors py-2">Contact</button>
            <button @click="scrollToSection('identifiants')" class="text-gray-custom hover:text-emerald transition-colors py-2">Identifiants</button>
            <router-link to="/admin" class="text-gray-custom hover:text-emerald transition-colors py-2">Admin</router-link>
          </div>
        </div>
      </nav>
    </header>

    <!-- Hero Section -->
    <section id="hero" class="min-h-screen flex items-center justify-center px-4 pt-16">
      <div class="text-center max-w-4xl">
        <h1 class="text-4xl sm:text-5xl md:text-6xl lg:text-7xl font-bold mb-4 sm:mb-6">
          <span class="text-emerald">Développeur</span><br>
          <span class="text-off-white">Web junior</span>
        </h1>
        <p class="text-base sm:text-lg md:text-xl lg:text-2xl text-gray-custom mb-6 sm:mb-8">
          Création d'applications web modernes avec des technologies de pointes
        </p>
        <div class="flex flex-col sm:flex-row gap-3 sm:gap-4 justify-center">
          <button 
            @click="scrollToSection('portfolio')"
            class="bg-emerald text-obsidian px-6 sm:px-8 py-2 sm:py-3 text-sm sm:text-base rounded-lg hover:bg-neon-lime transition-all transform hover:scale-105 font-semibold"
          >
            Voir mes projets
          </button>
          <button 
            @click="scrollToSection('contact')"
            class="border border-emerald text-emerald px-6 sm:px-8 py-2 sm:py-3 text-sm sm:text-base rounded-lg hover:bg-emerald hover:text-obsidian transition-all font-semibold"
          >
            Me contacter
          </button>
        </div>
        
        <!-- Technologies Stack -->
        <div class="mt-16 grid grid-cols-3 sm:grid-cols-6 gap-4">
          <div class="text-3xl" data-aos="fade-up" data-aos-delay="100">🐍</div>
          <div class="text-3xl" data-aos="fade-up" data-aos-delay="200">🎯</div>
          <div class="text-3xl" data-aos="fade-up" data-aos-delay="300">⚛️</div>
          <div class="text-3xl" data-aos="fade-up" data-aos-delay="400">🎨</div>
          <div class="text-3xl" data-aos="fade-up" data-aos-delay="500">🗄️</div>
          <div class="text-3xl" data-aos="fade-up" data-aos-delay="600">🚀</div>
        </div>
      </div>
    </section>

    <!-- Portfolio Section -->
    <section id="portfolio" class="py-20 px-4">
      <div class="max-w-7xl mx-auto">
        <div class="text-center mb-8 sm:mb-16 px-2 sm:px-0">
          <h2 class="text-3xl sm:text-4xl md:text-5xl font-bold text-off-white mb-4 sm:mb-6">Projets réalisés</h2>
          <p class="text-base sm:text-xl text-gray-custom">Découvrez mes réalisations récentes</p>
        </div>

        <!-- Filtres (supprimés pour simplification) -->

        <!-- Projets Grid - Centré -->
        <div v-if="projectsLoading" class="text-center py-12 text-gray-custom">
          Chargement des projets...
        </div>
        <div v-else-if="projectsError" class="text-center py-12">
          <p class="text-red-400 mb-4">{{ projectsError }}</p>
          <button
            @click="loadData"
            class="bg-emerald text-obsidian px-6 py-2 rounded-lg hover:bg-neon-lime transition-all font-semibold"
          >
            Réessayer
          </button>
        </div>
        <div v-else-if="filteredProjects.length === 0" class="text-center py-12 text-gray-custom">
          Aucun projet publié pour le moment.
        </div>
        <div v-else class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8 justify-items-center">
          <div 
            v-for="project in filteredProjects" 
            :key="project.id"
            class="bg-dark-jungle p-6 rounded-xl border border-gray-800 hover:border-emerald transition-all cursor-pointer w-full"
            @click="showProjectDetail(project)"
            data-aos="fade-up"
          >
            <div class="w-full h-32 sm:h-40 md:h-48 rounded-lg mb-4 overflow-hidden bg-gray-800">
              <img 
                v-if="project.image_url"
                :src="project.image_url" 
                :alt="project.project_name"
                class="w-full h-full object-cover"
                @error="(e) => e.target.style.display = 'none'"
              >
            </div>
            <h3 class="text-xl font-semibold mb-2 text-off-white">{{ project.project_name }}</h3>
            <p class="text-gray-custom mb-4">{{ project.project_description }}</p>
            <div class="flex flex-wrap gap-2 mb-4">
              <span v-for="tech in project.technology_used.split(',')" :key="tech"
                    class="px-3 py-1 bg-emerald/20 text-emerald rounded-full text-sm">
                {{ tech.trim() }}
              </span>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Services Section -->
    <section id="services" class="py-20 px-4 bg-dark-jungle">
      <div class="max-w-7xl mx-auto">
        <div class="text-center mb-16">
          <h2 class="text-4xl md:text-5xl font-bold text-off-white mb-6">Services</h2>
          <p class="text-xl text-gray-custom">Des solutions sur mesure pour votre entreprise</p>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-3 gap-6 md:gap-8">
          <div class="text-center p-4 sm:p-6 md:p-8" data-aos="fade-up" data-aos-delay="100">
            <div class="text-4xl sm:text-5xl mb-3 sm:mb-6">🖥️</div>
            <h3 class="text-lg sm:text-xl md:text-2xl font-semibold mb-2 sm:mb-4 text-emerald">Développement Web</h3>
            <p class="text-sm sm:text-base text-gray-custom">Sites vitrines, applications web, plateformes e-commerce</p>
          </div>
          <div class="text-center p-4 sm:p-6 md:p-8" data-aos="fade-up" data-aos-delay="200">
            <div class="text-4xl sm:text-5xl mb-3 sm:mb-6">🤖</div>
            <h3 class="text-lg sm:text-xl md:text-2xl font-semibold mb-2 sm:mb-4 text-emerald">Automatisation</h3>
            <p class="text-sm sm:text-base text-gray-custom">Scripts Python, web scraping, traitement de données</p>
          </div>
          <div class="text-center p-4 sm:p-6 md:p-8" data-aos="fade-up" data-aos-delay="300">
            <div class="text-4xl sm:text-5xl mb-3 sm:mb-6">🔧</div>
            <h3 class="text-lg sm:text-xl md:text-2xl font-semibold mb-2 sm:mb-4 text-emerald">Maintenance</h3>
            <p class="text-sm sm:text-base text-gray-custom">Audit, optimisation, corrections de bugs</p>
          </div>
        </div>
      </div>
    </section>

    <!-- Contact Section -->
    <section id="contact" class="py-20 px-4">
      <div class="max-w-4xl mx-auto">
        <div class="text-center mb-16">
          <h2 class="text-4xl md:text-5xl font-bold text-off-white mb-6">Contact</h2>
          <p class="text-xl text-gray-custom">Discutons de votre projet</p>
        </div>

        <form @submit.prevent="submitContact" class="space-y-6">
          <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
            <div>
              <label class="block text-sm font-medium text-gray-custom mb-2">Nom</label>
              <input
                v-model="contactForm.nom"
                type="text"
                required
                class="w-full px-3 sm:px-4 py-2 sm:py-3 bg-dark-jungle border border-gray-800 rounded-lg focus:outline-none focus:ring-2 focus:ring-emerald text-off-white text-sm sm:text-base"
                placeholder="Votre nom"
              />
            </div>
            <div>
              <label class="block text-sm font-medium text-gray-custom mb-2">Email</label>
              <input
                v-model="contactForm.email"
                type="email"
                required
                class="w-full px-3 sm:px-4 py-2 sm:py-3 bg-dark-jungle border border-gray-800 rounded-lg focus:outline-none focus:ring-2 focus:ring-emerald text-off-white text-sm sm:text-base"
                placeholder="votre@email.com"
              />
            </div>
          </div>
          
          <div>
            <label class="block text-sm font-medium text-gray-custom mb-2">Type de projet</label>
            <select
              v-model="contactForm.type_projet"
              required
              class="w-full px-3 sm:px-4 py-2 sm:py-3 bg-dark-jungle border border-gray-800 rounded-lg focus:outline-none focus:ring-2 focus:ring-emerald text-off-white text-sm sm:text-base"
            >
              <option value="">Sélectionnez...</option>
              <option value="Site vitrine">Site vitrine</option>
              <option value="Application web">Application web</option>
              <option value="E-commerce">E-commerce</option>
              <option value="Autre">Autre</option>
            </select>
          </div>

          <div>
            <label class="block text-sm font-medium text-gray-custom mb-2">Message</label>
            <textarea
              v-model="contactForm.message"
              required
              rows="6"
              class="w-full px-3 sm:px-4 py-2 sm:py-3 bg-dark-jungle border border-gray-800 rounded-lg focus:outline-none focus:ring-2 focus:ring-emerald text-off-white text-sm sm:text-base"
              placeholder="Décrivez votre projet..."
            ></textarea>
          </div>

          <div class="text-center">
            <button
              type="submit"
              :disabled="loading"
              class="bg-emerald text-obsidian px-6 sm:px-8 py-2 sm:py-3 text-sm sm:text-base rounded-lg hover:bg-neon-lime transition-all transform hover:scale-105 font-semibold disabled:opacity-50"
            >
              <span v-if="!loading">Envoyer le message</span>
              <span v-else>Envoi en cours...</span>
            </button>
          </div>
        </form>

        <div v-if="successMessage" class="mt-6 p-4 bg-emerald/20 border border-emerald rounded-lg text-emerald text-center">
          {{ successMessage }}
        </div>
      </div>
    </section>

    <!-- Identifiants Section -->
    <section id="identifiants" class="py-20 px-4 bg-dark-jungle">
      <div class="max-w-7xl mx-auto">
        <div class="text-center mb-16">
          <h2 class="text-4xl md:text-5xl font-bold text-off-white mb-6">Identifiants Personnel</h2>
          <p class="text-xl text-gray-custom">Retrouvez-moi sur les plateformes professionnelles</p>
        </div>

        <!-- Cartes Identifiants - Centrées -->
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8 justify-items-center">
          <!-- GitHub -->
          <div class="text-center p-6 bg-obsidian rounded-xl border border-gray-800 hover:border-emerald transition-all w-full" data-aos="fade-up" data-aos-delay="100">
            <img src="@/assets/icones/github.png" alt="GitHub" class="h-16 w-16 mx-auto mb-4 object-contain">
            <h3 class="text-xl font-semibold mb-3 text-emerald">GitHub</h3>
            <p class="text-gray-custom mb-4">Mon portfolio de projets open source</p>
            <a 
              href="https://github.com/bradyFrasnel" 
              target="_blank"
              class="inline-flex items-center gap-2 bg-emerald text-obsidian px-4 sm:px-6 py-2 text-sm sm:text-base rounded-lg hover:bg-neon-lime transition-all font-semibold"
            >
              <span>Voir GitHub</span>
              <span>→</span>
            </a>
          </div>

          <!-- LinkedIn -->
          <div class="text-center p-6 bg-obsidian rounded-xl border border-gray-800 hover:border-emerald transition-all w-full" data-aos="fade-up" data-aos-delay="200">
            <img src="@/assets/icones/linkedin.png" alt="LinkedIn" class="h-16 w-16 mx-auto mb-4 object-contain">
            <h3 class="text-xl font-semibold mb-3 text-emerald">LinkedIn</h3>
            <p class="text-gray-custom mb-4">Mon profil professionnel et expériences</p>
            <a 
              href="https://linkedin.com/in/brady-frasnel" 
              target="_blank"
              class="inline-flex items-center gap-2 bg-emerald text-obsidian px-4 sm:px-6 py-2 text-sm sm:text-base rounded-lg hover:bg-neon-lime transition-all font-semibold"
            >
              <span>Voir LinkedIn</span>
              <span>→</span>
            </a>
          </div>

          <!-- Email -->
          <div class="text-center p-6 bg-obsidian rounded-xl border border-gray-800 hover:border-emerald transition-all w-full" data-aos="fade-up" data-aos-delay="300">
            <img src="@/assets/icones/mail.png" alt="Email" class="h-16 w-16 mx-auto mb-4 object-contain">
            <h3 class="text-xl font-semibold mb-3 text-emerald">Email</h3>
            <p class="text-gray-custom mb-4">Contact direct pour vos projets</p>
            <a 
              href="mailto:mokumabrady13@gmail.com" 
              class="inline-flex items-center gap-2 bg-emerald text-obsidian px-4 sm:px-6 py-2 text-sm sm:text-base rounded-lg hover:bg-neon-lime transition-all font-semibold truncate"
            >
              <span class="truncate">mokumabrady13@gmail.com</span>
              <span>→</span>
            </a>
          </div>

          <!-- WhatsApp -->
          <div class="text-center p-6 bg-obsidian rounded-xl border border-gray-800 hover:border-emerald transition-all w-full" data-aos="fade-up" data-aos-delay="400">
            <img src="@/assets/icones/whatsApp2.png" alt="WhatsApp" class="h-16 w-16 mx-auto mb-4 object-contain">
            <h3 class="text-xl font-semibold mb-3 text-emerald">WhatsApp</h3>
            <p class="text-gray-custom mb-4">Discutez directement avec moi</p>
            <a 
              href="https://wa.me/33XXXXXXXXX" 
              target="_blank"
              class="inline-flex items-center gap-2 bg-emerald text-obsidian px-4 sm:px-6 py-2 text-sm sm:text-base rounded-lg hover:bg-neon-lime transition-all font-semibold"
            >
              <span>Ouvrir WhatsApp</span>
              <span>→</span>
            </a>
          </div>
        </div>

        <!-- Informations additionnelles -->
        <div class="mt-16 text-center">
          <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
            <div class="bg-obsidian p-6 rounded-xl border border-gray-800">
            <img src="@/assets/icones/localisation.png" alt="Localisation" class="h-8 w-8 inline-block mr-2">Localisation
              <p class="text-gray-custom">Disponible pour missions en remote et sur Paris</p>
            </div>
            <div class="bg-obsidian p-6 rounded-xl border border-gray-800">
              <h4 class="text-lg font-semibold mb-3 text-emerald">⚡ Disponibilité</h4>
              <p class="text-gray-custom">Ouvert aux projets freelance et collaborations</p>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Modal Détail Projet -->
    <div 
      v-if="selectedProject" 
      class="fixed inset-0 bg-black/80 flex items-center justify-center p-4 z-50"
      @click="closeProjectDetail"
    >
      <div class="bg-dark-jungle rounded-xl p-4 sm:p-6 md:p-8 max-w-2xl w-full max-h-[90vh] overflow-y-auto" @click.stop>
        <div class="flex flex-col sm:flex-row sm:justify-between sm:items-start mb-4 sm:mb-6 gap-2">
          <h3 class="text-xl sm:text-2xl font-bold text-off-white">{{ selectedProject.project_name }}</h3>
          <button 
            @click="closeProjectDetail"
            class="self-end sm:self-auto text-gray-custom hover:text-off-white text-2xl"
          >
            ✕
          </button>
        </div>
        
        <div v-if="selectedProject.image_url" class="w-full aspect-video rounded-lg mb-6 overflow-hidden bg-gray-800">
          <img 
            :src="selectedProject.image_url" 
            :alt="selectedProject.project_name"
            class="w-full h-full object-cover"
            @error="(e) => e.target.style.display = 'none'"
          >
        </div>
        
        <p class="text-gray-custom mb-6">{{ selectedProject.project_description }}</p>
        
        <div class="flex flex-wrap gap-2 mb-6">
          <span v-for="tech in selectedProject.technology_used.split(',')" :key="tech"
                class="px-3 py-1 bg-emerald/20 text-emerald rounded-full text-sm">
            {{ tech.trim() }}
          </span>
        </div>
        
        <div class="flex flex-col sm:flex-row gap-3 sm:gap-4">
          <a 
            v-if="selectedProject.github_link"
            :href="selectedProject.github_link"
            target="_blank"
            class="bg-emerald text-obsidian px-4 sm:px-6 py-2 text-sm sm:text-base rounded-lg hover:bg-neon-lime transition-all text-center"
          >
            Voir le code
          </a>
          <a 
            v-if="selectedProject.demo_link"
            :href="selectedProject.demo_link"
            target="_blank"
            class="border border-emerald text-emerald px-4 sm:px-6 py-2 text-sm sm:text-base rounded-lg hover:bg-emerald hover:text-obsidian transition-all text-center"
          >
            Voir la démo
          </a>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, computed } from 'vue'
import api from '../services/api.js'
import { parseProjectsResponse } from '../utils/projects.js'

const isDarkMode = ref(true)
const mobileMenuOpen = ref(false)
const loading = ref(false)
const successMessage = ref('')
const selectedProject = ref(null)

const projects = ref([])
const projectsLoading = ref(true)
const projectsError = ref('')

const contactForm = ref({
  nom: '',
  email: '',
  type_projet: '',
  message: ''
})

const filteredProjects = computed(() => {
  return projects.value
})

const toggleDarkMode = () => {
  isDarkMode.value = !isDarkMode.value
  document.documentElement.classList.toggle('dark')
}

const toggleMobileMenu = () => {
  mobileMenuOpen.value = !mobileMenuOpen.value
}

const scrollToSection = (sectionId) => {
  const element = document.getElementById(sectionId)
  if (element) {
    element.scrollIntoView({ behavior: 'smooth' })
    mobileMenuOpen.value = false
  }
}

const filterProjects = (categoryId) => {
  // Fonction conservée pour compatibilité mais non utilisée
  console.log('Filtrage désactivé')
}

const showProjectDetail = (project) => {
  selectedProject.value = project
}

const closeProjectDetail = () => {
  selectedProject.value = null
}

const submitContact = async () => {
  loading.value = true
  successMessage.value = ''
  
  try {
    await api.sendContact(contactForm.value)
    successMessage.value = 'Message envoyé avec succès !'
    contactForm.value = { nom: '', email: '', type_projet: '', message: '' }
  } catch (error) {
    successMessage.value = 'Erreur lors de l\'envoi du message'
  } finally {
    loading.value = false
    setTimeout(() => {
      successMessage.value = ''
    }, 5000)
  }
}

const loadData = async () => {
  projectsLoading.value = true
  projectsError.value = ''
  try {
    const projectsResponse = await api.getProjects()
    projects.value = parseProjectsResponse(projectsResponse.data)
  } catch (error) {
    console.error('Erreur chargement données:', error)
    projectsError.value = 'Impossible de charger les projets. Le serveur peut être en cours de démarrage.'
  } finally {
    projectsLoading.value = false
  }
}

onMounted(() => {
  document.documentElement.classList.add('dark')
  loadData()
  
  // Initialiser AOS si disponible
  if (typeof AOS !== 'undefined') {
    AOS.init()
  }
})
</script>
