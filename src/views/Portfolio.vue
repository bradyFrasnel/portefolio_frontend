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
      <section class="mb-8">
        <h2 class="text-3xl font-bold text-center text-off-white mb-8">Découvrez mes réalisations</h2>
        
        <!-- Filtres et recherche -->
        <div class="bg-dark-jungle p-6 rounded-xl border border-gray-800 mb-8" data-aos="fade-up">
          <div class="grid md:grid-cols-2 gap-4 mb-4">
            <div>
              <label class="block text-sm font-medium text-gray-custom mb-2">Recherche</label>
              <input
                v-model="searchQuery"
                @input="searchProjects"
                type="text"
                placeholder="Rechercher un projet..."
                class="w-full px-4 py-2 bg-obsidian border border-gray-700 rounded-lg text-off-white focus:border-emerald focus:outline-none"
              />
            </div>
            <div>
              <label class="block text-sm font-medium text-gray-custom mb-2">Recherche</label>
              <input
                v-model="searchQuery"
                @input="searchProjects"
                type="text"
                placeholder="Rechercher un projet..."
                class="w-full px-4 py-2 bg-obsidian border border-gray-700 rounded-lg text-off-white focus:border-emerald focus:outline-none"
              />
            </div>
          </div>
        </div>
      </section>

      <div v-if="loading" class="text-center py-12">
        <div class="inline-block animate-spin rounded-full h-12 w-12 border-b-2 border-indigo-600"></div>
        <p class="mt-4 text-gray-600">Chargement des projets...</p>
      </div>

      <div v-else-if="error" class="text-center py-12">
        <div class="text-red-600 text-xl mb-4">❌</div>
        <p class="text-gray-600">{{ error }}</p>
      </div>

      <div v-else class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6 sm:gap-8">
        <div 
          v-for="project in projects" 
          :key="project.id"
          class="bg-white rounded-xl shadow-lg overflow-hidden hover:shadow-xl transition-shadow cursor-pointer"
          @click="goToProject(project.id)"
          data-aos="fade-up"
          :data-aos-delay="projects.indexOf(project) * 100"
        >
          <img 
            :src="projectImageSrc(project, 'card')" 
            :alt="project.project_name"
            class="h-40 sm:h-48 w-full object-cover"
            @error="(e) => handleImageError(e, 'card')"
          >
          <div class="p-4 sm:p-6">
            <h3 class="text-lg sm:text-xl font-semibold mb-2">{{ project.project_name }}</h3>
            <p class="text-gray-600 text-sm sm:text-base mb-4 line-clamp-3">{{ project.project_description }}</p>
            <div class="flex flex-wrap gap-2 mb-4">
              <span 
                v-for="tech in project.technology_used.split(',')" 
                :key="tech"
                class="px-2 py-1 sm:px-3 sm:py-1 bg-emerald-100 text-emerald-700 rounded-full text-xs sm:text-sm"
              >
                {{ tech.trim() }}
              </span>
            </div>
            <div class="flex justify-between items-center">
              <span class="text-xs sm:text-sm text-gray-500">{{ project.date || '2024' }}</span>
              <button class="text-emerald-600 hover:text-emerald-800 font-medium text-sm sm:text-base">
                Voir plus →
              </button>
            </div>
          </div>
        </div>
      </div>

      <!-- Pagination -->
      <div v-if="totalPages > 1" class="flex justify-center mt-8 space-x-2" data-aos="fade-up">
        <button
          v-for="page in totalPages"
          :key="page"
          @click="changePage(page)"
          :class="[
            'px-4 py-2 rounded-lg transition-colors',
            currentPage === page 
              ? 'bg-emerald text-obsidian' 
              : 'bg-dark-jungle text-gray-custom hover:bg-gray-800'
          ]"
        >
          {{ page }}
        </button>
      </div>
    </main>
    
    <!-- Footer -->
    <Footer />
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import api from '../services/api.js'
import Footer from '../components/Footer.vue'
import { projectImageSrc, handleImageError } from '../utils/placeholders.js'

const router = useRouter()
const projects = ref([])
const categories = ref([])
const selectedCategory = ref('')
const searchQuery = ref('')
const loading = ref(true)
const error = ref(null)
const currentPage = ref(1)
const totalPages = ref(1)

const goToProject = (projectId) => {
  router.push(`/project/${projectId}`)
}

const fetchProjects = async () => {
  try {
    loading.value = true
    const response = await api.getProjects(currentPage.value, searchQuery.value)
    projects.value = response.data.results
    totalPages.value = Math.ceil(response.data.count / 12)
    error.value = null
  } catch (err) {
    console.error('Erreur:', err)
    // Données de démonstration si le backend n'est pas encore accessible
    projects.value = [
      { id: 1, title: 'Projet E-commerce', description: 'Site e-commerce moderne avec Vue.js et Django', technologies: ['Vue.js', 'Django', 'PostgreSQL'], category: 'Site Vitrine', date: '2024' },
      { id: 2, title: 'Application Mobile', description: 'App iOS/Android avec React Native et Django REST', technologies: ['React Native', 'Django REST', 'PostgreSQL'], category: 'Application Web', date: '2024' },
      { id: 3, title: 'Portfolio Personnel', description: 'Site portfolio responsive et moderne avec animations', technologies: ['Vue.js', 'Tailwind CSS', 'AOS'], category: 'Site Vitrine', date: '2023' }
    ]
    error.value = null
  } finally {
    loading.value = false
  }
}

const fetchCategories = async () => {
  // Supprimé car non supporté par la nouvelle API
}

const filterByCategory = (category) => {
  selectedCategory.value = category
  currentPage.value = 1
  fetchProjects()
}

const searchProjects = () => {
  currentPage.value = 1
  fetchProjects()
}

const changePage = (page) => {
  currentPage.value = page
  fetchProjects()
}

onMounted(() => {
  fetchCategories()
  fetchProjects()
})
</script>
