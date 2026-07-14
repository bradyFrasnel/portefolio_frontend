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
      <div v-if="loading" class="text-center py-12">
        <div class="inline-block animate-spin rounded-full h-12 w-12 border-b-2 border-indigo-600"></div>
        <p class="mt-4 text-gray-600">Chargement du projet...</p>
      </div>

      <div v-else-if="error" class="text-center py-12">
        <div class="text-red-600 text-xl mb-4">❌</div>
        <p class="text-gray-600">{{ error }}</p>
        <router-link to="/portfolio" class="inline-block mt-4 text-indigo-600 hover:text-indigo-800">
          ← Retour au portfolio
        </router-link>
      </div>

      <div v-else-if="project" class="bg-white rounded-xl shadow-lg overflow-hidden">
        <img 
          :src="projectImageSrc(project, 'detail')" 
          :alt="project.project_name"
          class="h-64 h-full w-full object-cover"
          @error="(e) => handleImageError(e, 'detail')"
        >
        
        <div class="p-8">
          <div class="mb-6">
            <router-link to="/portfolio" class="text-indigo-600 hover:text-indigo-800 mb-4 inline-block">
              ← Retour au portfolio
            </router-link>
          </div>

          <h1 class="text-3xl md:text-4xl font-bold text-gray-900 mb-4">
            {{ project.project_name }}
          </h1>

          <div class="flex flex-wrap gap-2 mb-6">
            <span 
              v-for="tech in project.technology_used.split(',')" 
              :key="tech"
              class="px-4 py-2 bg-indigo-100 text-indigo-700 rounded-full"
            >
              {{ tech.trim() }}
            </span>
          </div>

          <div class="prose max-w-none mb-8">
            <h2 class="text-2xl font-semibold mb-4">Description</h2>
            <p class="text-gray-600 text-lg leading-relaxed">
              {{ project.project_description }}
            </p>
          </div>

          <div class="grid md:grid-cols-2 gap-8 mb-8">
            <div>
              <h3 class="text-xl font-semibold mb-4">Objectifs</h3>
              <ul class="space-y-2 text-gray-600">
                <li class="flex items-start">
                  <span class="text-indigo-600 mr-2">✓</span>
                  {{ project.objective1 || 'Créer une interface utilisateur moderne et intuitive' }}
                </li>
                <li class="flex items-start">
                  <span class="text-indigo-600 mr-2">✓</span>
                  {{ project.objective2 || 'Optimiser les performances et l\'expérience utilisateur' }}
                </li>
                <li class="flex items-start">
                  <span class="text-indigo-600 mr-2">✓</span>
                  {{ project.objective3 || 'Assurer la compatibilité multi-appareils' }}
                </li>
              </ul>
            </div>

            <div>
              <h3 class="text-xl font-semibold mb-4">Technologies utilisées</h3>
              <div class="space-y-2">
                <div class="flex justify-between py-2 border-b">
                  <span class="text-gray-600">Frontend</span>
                  <span class="font-medium">{{ project.frontend || 'Vue.js 3, Tailwind CSS' }}</span>
                </div>
                <div class="flex justify-between py-2 border-b">
                  <span class="text-gray-600">Backend</span>
                  <span class="font-medium">{{ project.backend || 'Node.js, Express' }}</span>
                </div>
                <div class="flex justify-between py-2 border-b">
                  <span class="text-gray-600">Base de données</span>
                  <span class="font-medium">{{ project.database || 'MongoDB' }}</span>
                </div>
                <div class="flex justify-between py-2">
                  <span class="text-gray-600">Déploiement</span>
                  <span class="font-medium">{{ project.deployment || 'Vercel, Render' }}</span>
                </div>
              </div>
            </div>
          </div>

          <div class="flex flex-col sm:flex-row gap-4">
            <a 
              v-if="project.demo_link"
              :href="project.demo_link" 
              target="_blank"
              class="bg-indigo-600 text-white px-6 py-3 rounded-lg hover:bg-indigo-700 transition-colors text-center"
            >
              Voir la démo →
            </a>
            <a 
              v-if="project.github_link"
              :href="project.github_link" 
              target="_blank"
              class="border border-indigo-600 text-indigo-600 px-6 py-3 rounded-lg hover:bg-indigo-50 transition-colors text-center"
            >
              Voir le code →
            </a>
          </div>
        </div>
      </div>
    </main>
    
    <!-- Footer -->
    <Footer />
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import api from '../services/api.js'
import Footer from '../components/Footer.vue'
import { projectImageSrc, handleImageError } from '../utils/placeholders.js'

const route = useRoute()
const router = useRouter()
const { id } = route.params

const project = ref(null)
const loading = ref(true)
const error = ref(null)

const fetchProject = async () => {
  try {
    loading.value = true
    const response = await api.getProject(id)
    project.value = response.data
    error.value = null
  } catch (err) {
    console.error('Erreur:', err)
    // Données de démonstration si le backend n'est pas encore accessible
    project.value = {
      id: parseInt(id),
      title: `Projet ${id}`,
      description: 'Description détaillée de ce projet innovant qui met en œuvre les meilleures pratiques de développement web moderne avec Vue.js et Django.',
      long_description: 'Ce projet démontre mes compétences en développement fullstack avec une architecture headless moderne. J\'ai implémenté une API REST robuste avec Django REST Framework et une interface utilisateur réactive avec Vue.js 3.',
      technologies: ['Vue.js', 'Django', 'Tailwind CSS', 'PostgreSQL'],
      category: 'Site Vitrine',
      date: '2024',
      github_url: 'https://github.com',
      demo_url: 'https://example.com',
      challenges: 'Optimisation des performances et gestion des états complexes',
      solutions: 'Utilisation de Vue Composition API et cache Redis'
    }
    error.value = null
  } finally {
    loading.value = false
  }
}

onMounted(() => {
  fetchProject()
})
</script>
