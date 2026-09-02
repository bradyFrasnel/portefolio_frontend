<template>
  <div class="min-h-screen bg-gray-50 dark:bg-gray-900 text-white p-8 flex flex-col relative">
    
    <!-- Toast Notification -->
    <div v-if="toast.show" 
         :class="['fixed top-4 right-4 z-[60] px-6 py-3 rounded-xl shadow-lg transition-all transform', 
                  toast.type === 'success' ? 'bg-emerald-500 text-white' : 'bg-red-500 text-white']">
      {{ toast.message }}
    </div>

    <!-- Confirmation Modal -->
    <div v-if="showDeleteConfirm" class="fixed inset-0 bg-black/60 backdrop-blur-sm z-[60] flex items-center justify-center p-4">
      <div class="bg-gray-200 dark:bg-gray-800 rounded-3xl p-6 md:p-8 max-w-sm w-full shadow-2xl border border-white/10">
        <h3 class="text-xl font-bold text-white mb-4">Confirmer la suppression</h3>
        <p class="text-gray-700 dark:text-gray-300 mb-6">Voulez-vous vraiment supprimer cet élément ? Cette action est irréversible.</p>
        <div class="flex justify-end gap-3">
          <button @click="showDeleteConfirm = false" class="px-4 py-2 bg-gray-100 dark:bg-gray-700 hover:bg-gray-600 text-white rounded-xl text-sm transition-colors">Annuler</button>
          <button @click="confirmDelete" class="px-4 py-2 bg-red-600 hover:bg-red-700 text-white rounded-xl text-sm transition-colors">Supprimer</button>
        </div>
      </div>
    </div>

    <div class="w-full max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 flex-1 flex flex-col justify-center">
      <div class="flex justify-end mb-6">
        <button 
          v-if="isLoggedIn" 
          @click="logout" 
          class="bg-red-600 hover:bg-red-700 text-white px-3 py-1.5 rounded-full text-xs font-semibold transition duration-200 shadow-sm shadow-black/20"
        >
          Déconnexion
        </button>
      </div>

      <!-- Connexion -->
      <div v-if="!isLoggedIn" class="bg-gray-200 dark:bg-gray-800 rounded-3xl p-6 md:p-8 mb-8 w-full max-w-sm mx-auto shadow-xl shadow-black/20 border border-white/10">
        <h2 class="text-xl font-semibold mb-5 text-emerald-500">Connexion Admin</h2>
        <form @submit.prevent="login" class="space-y-4">
          <div>
            <label class="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-2">Nom d'utilisateur</label>
            <input
              v-model="loginForm.username"
              type="text"
              required
              class="w-full px-3 py-2 text-sm bg-gray-100 dark:bg-gray-700 border border-gray-300 dark:border-gray-600 rounded-xl focus:outline-none focus:ring-2 focus:ring-emerald-500 text-white"
              placeholder="admin"
            />
          </div>
          <div class="relative">
            <label class="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-2">Mot de passe</label>
            <div class="relative">
              <input
                v-model="loginForm.password"
                :type="showPassword ? 'text' : 'password'"
                required
                class="w-full px-3 py-2 text-sm bg-gray-100 dark:bg-gray-700 border border-gray-300 dark:border-gray-600 rounded-xl focus:outline-none focus:ring-2 focus:ring-emerald-500 text-white pr-10"
                placeholder="••••••••"
              />
              <button
                type="button"
                @click="showPassword = !showPassword"
                class="absolute inset-y-0 right-0 pr-3 flex items-center text-gray-500 dark:text-gray-400 hover:text-emerald-500 focus:outline-none"
              >
                <!-- Eye icon (visible) -->
                <svg v-if="!showPassword" xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" viewBox="0 0 20 20" fill="currentColor">
                  <path d="M10 12a2 2 0 100-4 2 2 0 000 4z" />
                  <path fill-rule="evenodd" d="M.458 10C1.732 5.943 5.522 3 10 3s8.268 2.943 9.542 7c-1.274 4.057-5.064 7-9.542 7S1.732 14.057.458 10zM14 10a4 4 0 11-8 0 4 4 0 018 0z" clip-rule="evenodd" />
                </svg>
                <!-- Eye-off icon (hidden) -->
                <svg v-else xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" viewBox="0 0 20 20" fill="currentColor">
                  <path fill-rule="evenodd" d="M3.707 2.293a1 1 0 00-1.414 1.414l14 14a1 1 0 001.414-1.414l-1.473-1.473A10.014 10.014 0 0019.542 10C18.268 5.943 14.478 3 10 3a9.958 9.958 0 00-4.512 1.074l-1.78-1.781zm4.261 4.26a4 4 0 015.99 5.99l-5.99-5.99z" clip-rule="evenodd" />
                  <path d="M12.454 13.868l1.762 1.763A9.963 9.963 0 0110 17c-4.478 0-8.268-2.943-9.542-7a10.014 10.014 0 012.138-3.393l1.326 1.326a4 4 0 005.532 5.532z" />
                </svg>
              </button>
            </div>
          </div>
          <div v-if="error" class="text-red-500 text-sm mt-2">{{ error }}</div>
          <button
            type="submit"
            :disabled="loading"
            class="w-full bg-emerald-600 hover:bg-emerald-700 text-white font-semibold py-2.5 rounded-xl transition duration-200 text-sm shadow-lg shadow-emerald-500/20"
          >
            <span v-if="!loading">Se connecter</span>
            <span v-else>Connexion...</span>
          </button>
        </form>
      </div>
      <!-- Tableau de bord -->
      <div v-if="isLoggedIn" class="space-y-8">
        <!-- Cartes statistiques -->
        <div class="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-4 gap-4 mb-8">
          <!-- Total Projets -->
          <div class="bg-gradient-to-br from-emerald-500/10 to-emerald-600/5 backdrop-blur-md rounded-2xl p-6 border border-emerald-500/20 hover:border-emerald-500/40 transition-all hover:scale-105 cursor-pointer">
            <div class="flex items-center justify-between mb-2">
              <div class="p-3 bg-emerald-500/20 rounded-xl">
                <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6 text-emerald-400" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 11H5m14 0a2 2 0 012 2v6a2 2 0 01-2 2H5a2 2 0 01-2-2v-6a2 2 0 012-2m14 0V9a2 2 0 00-2-2M5 11V9a2 2 0 012-2m0 0V5a2 2 0 012-2h6a2 2 0 012 2v2M7 7h10" />
                </svg>
              </div>
              <span class="text-emerald-400 text-xs font-bold">+{{ projectsThisMonth }}</span>
            </div>
            <h3 class="text-gray-500 dark:text-gray-400 text-sm font-medium mb-1">Total Projets</h3>
            <p class="text-3xl font-black text-white">{{ projects.length }}</p>
          </div>

          <!-- Technologies utilisées -->
          <div class="bg-gradient-to-br from-blue-500/10 to-blue-600/5 backdrop-blur-md rounded-2xl p-6 border border-blue-500/20 hover:border-blue-500/40 transition-all hover:scale-105 cursor-pointer">
            <div class="flex items-center justify-between mb-2">
              <div class="p-3 bg-blue-500/20 rounded-xl">
                <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6 text-blue-400" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 20l4-16m4 4l4 4-4 4M6 16l-4-4 4-4" />
                </svg>
              </div>
              <span class="text-blue-400 text-xs font-bold">STACK</span>
            </div>
            <h3 class="text-gray-500 dark:text-gray-400 text-sm font-medium mb-1">Technologies</h3>
            <p class="text-3xl font-black text-white">{{ uniqueTechnologies }}</p>
          </div>

          <!-- Projets avec GitHub -->
          <div class="bg-gradient-to-br from-purple-500/10 to-purple-600/5 backdrop-blur-md rounded-2xl p-6 border border-purple-500/20 hover:border-purple-500/40 transition-all hover:scale-105 cursor-pointer">
            <div class="flex items-center justify-between mb-2">
              <div class="p-3 bg-purple-500/20 rounded-xl">
                <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6 text-purple-400" fill="currentColor" viewBox="0 0 24 24">
                  <path d="M12 0C5.37 0 0 5.37 0 12c0 5.31 3.435 9.795 8.205 11.385.6.105.825-.255.825-.57 0-.285-.015-1.23-.015-2.235-3.015.555-3.795-.735-4.035-1.41-.135-.345-.72-1.41-1.23-1.695-.42-.225-1.02-.78-.015-.795.945-.015 1.62.87 1.845 1.23 1.08 1.815 2.805 1.305 3.495.99.105-.78.42-1.305.765-1.605-2.67-.3-5.46-1.335-5.46-5.925 0-1.305.465-2.385 1.23-3.225-.12-.3-.54-1.53.12-3.18 0 0 1.005-.315 3.3 1.23.96-.27 1.98-.405 3-.405s2.04.135 3 .405c2.295-1.56 3.3-1.23 3.3-1.23.66 1.65.24 2.88.12 3.18.765.84 1.23 1.905 1.23 3.225 0 4.605-2.805 5.625-5.475 5.925.435.375.81 1.095.81 2.22 0 1.605-.015 2.895-.015 3.3 0 .315.225.69.825.57A12.02 12.02 0 0024 12c0-6.63-5.37-12-12-12z"/>
                </svg>
              </div>
              <span class="text-purple-400 text-xs font-bold">{{ projectsWithGithubPercent }}%</span>
            </div>
            <h3 class="text-gray-500 dark:text-gray-400 text-sm font-medium mb-1">Sur GitHub</h3>
            <p class="text-3xl font-black text-white">{{ projectsWithGithub }}</p>
          </div>

          <!-- Projets avec Demo -->
          <div class="bg-gradient-to-br from-orange-500/10 to-orange-600/5 backdrop-blur-md rounded-2xl p-6 border border-orange-500/20 hover:border-orange-500/40 transition-all hover:scale-105 cursor-pointer">
            <div class="flex items-center justify-between mb-2">
              <div class="p-3 bg-orange-500/20 rounded-xl">
                <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6 text-orange-400" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 12a9 9 0 01-9 9m9-9a9 9 0 00-9-9m9 9H3m9 9a9 9 0 01-9-9m9 9c1.657 0 3-4.03 3-9s-1.343-9-3-9m0 18c-1.657 0-3-4.03-3-9s1.343-9 3-9m-9 9a9 9 0 019-9" />
                </svg>
              </div>
              <span class="text-orange-400 text-xs font-bold">LIVE</span>
            </div>
            <h3 class="text-gray-500 dark:text-gray-400 text-sm font-medium mb-1">Avec Demo</h3>
            <p class="text-3xl font-black text-white">{{ projectsWithDemo }}</p>
          </div>
        </div>

        <!-- Graphiques ECharts -->
        <div class="grid grid-cols-1 lg:grid-cols-2 gap-6 mb-8">
          <!-- Graphique Visiteurs -->
          <div class="bg-gray-200 dark:bg-gray-800/50 backdrop-blur-md rounded-2xl p-6 border border-white/5">
            <h3 class="text-xl font-bold text-white mb-4 flex items-center">
              <span class="w-2 h-6 bg-emerald-500 rounded-full mr-3"></span>
              Visiteurs (30 derniers jours)
            </h3>
            <v-chart :option="visitorsChartOption" autoresize class="h-80" />
          </div>

          <!-- Graphique Projets les plus vus -->
          <div class="bg-gray-200 dark:bg-gray-800/50 backdrop-blur-md rounded-2xl p-6 border border-white/5">
            <h3 class="text-xl font-bold text-white mb-4 flex items-center">
              <span class="w-2 h-6 bg-blue-500 rounded-full mr-3"></span>
              Projets les plus vus
            </h3>
            <v-chart :option="topProjectsChartOption" autoresize class="h-80" />
          </div>
        </div>

        <!-- Actions Rapides -->
        <div class="bg-gray-200 dark:bg-gray-800/50 backdrop-blur-md rounded-2xl p-6 border border-white/5 mb-8">
          <h3 class="text-xl font-bold text-white mb-4 flex items-center">
            <span class="w-2 h-6 bg-purple-500 rounded-full mr-3"></span>
            Actions Rapides
          </h3>
          <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
            <button
              @click="openCreateForm"
              class="flex items-center justify-center space-x-3 bg-gradient-to-r from-emerald-600 to-emerald-500 hover:from-emerald-500 hover:to-emerald-400 text-white py-3 rounded-2xl transition-all shadow-lg shadow-emerald-500/20 font-semibold hover:scale-[1.02] text-sm"
            >
              <span class="flex justify-center"><Plus :size="24" /></span>
              <span>Ajouter un projet</span>
            </button>
            <button
              @click="refreshData"
              class="flex items-center justify-center space-x-3 bg-gradient-to-r from-blue-600 to-blue-500 hover:from-blue-500 hover:to-blue-400 text-white py-3 rounded-2xl transition-all shadow-lg shadow-blue-500/20 font-semibold hover:scale-[1.02] text-sm"
            >
              <span class="flex justify-center"><RefreshCw class="group-hover:rotate-180 transition-transform duration-500" :size="24" /></span>
              <span>Rafraîchir</span>
            </button>
            <button
              @click="goToApiDocs"
              class="flex items-center justify-center space-x-3 bg-gradient-to-r from-purple-600 to-purple-500 hover:from-purple-500 hover:to-purple-400 text-white py-3 rounded-2xl transition-all shadow-lg shadow-purple-500/20 font-semibold hover:scale-[1.02] text-sm"
            >
              <span class="flex justify-center"><BookOpen :size="24" /></span>
              <span>API Docs</span>
            </button>
          </div>
        </div>
      </div>

      <!-- Formulaire de création de projet -->
      <div v-if="showCreateForm" class="mt-8 bg-gray-200 dark:bg-gray-800 rounded-3xl p-5 md:p-6 max-w-2xl mx-auto shadow-lg shadow-black/20">
        <h3 class="text-xl md:text-2xl font-bold mb-5 text-emerald-500">{{ editingProject ? 'Modifier le projet' : 'Déposer un Nouveau Projet' }}</h3>
        <form @submit.prevent="createProject" class="space-y-4 text-sm">
          <div>
            <label class="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-2">Titre du Projet</label>
            <input
              v-model="projectForm.project_name"
              type="text"
              required
              class="w-full px-3 py-2 text-sm bg-gray-100 dark:bg-gray-700 border border-gray-300 dark:border-gray-600 rounded-xl focus:outline-none focus:ring-2 focus:ring-emerald-500 text-white"
              placeholder="Ex: Portfolio Moderne"
            />
          </div>
          
          <div>
            <label class="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-2">Image du projet (Upload Cloudinary)</label>
            <div class="flex flex-col md:flex-row md:items-center gap-4">
              <label class="flex-1 cursor-pointer">
                <div class="flex items-center justify-center px-3 py-2 bg-gray-100 dark:bg-gray-700 border border-gray-300 dark:border-gray-600 rounded-xl hover:bg-gray-600 transition-colors text-gray-700 dark:text-gray-300 text-sm">
                  <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 mr-2" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-8l-4-4m0 0L8 8m4-4v12" />
                  </svg>
                  <span>{{ projectForm.project_image && projectForm.project_image.name ? projectForm.project_image.name : 'Choisir une image...' }}</span>
                </div>
                <input
                  type="file"
                  @change="handleFileChange"
                  accept="image/*"
                  class="hidden"
                />
              </label>
              <button 
                v-if="projectForm.project_image" 
                type="button" 
                @click="projectForm.project_image = ''; localPreview = ''"
                class="text-red-500 hover:text-red-400 text-sm font-semibold"
              >
                Annuler
              </button>
            </div>
            
            <!-- Previsualisation image -->
            <div v-if="imagePreviewUrl" class="mt-4">
              <p class="text-xs text-gray-500 dark:text-gray-400 mb-2">Aperçu :</p>
              <img :src="imagePreviewUrl" class="h-36 rounded-xl border border-white/10 object-cover shadow-lg" />
            </div>
          </div>
          
          <div>
            <label class="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-2">Description</label>
            <textarea
              v-model="projectForm.project_description"
              required
              rows="4"
              class="w-full px-3 py-2 text-sm bg-gray-100 dark:bg-gray-700 border border-gray-300 dark:border-gray-600 rounded-xl focus:outline-none focus:ring-2 focus:ring-emerald-500 text-white"
              placeholder="Description complète du projet"
            ></textarea>
          </div>
          
          <div>
            <label class="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-2">Technologies (Cochez celles utilisées)</label>
            <div class="grid grid-cols-2 gap-2 mt-2 max-h-40 overflow-y-auto p-2 bg-gray-200 dark:bg-gray-800 rounded-lg border border-gray-300 dark:border-gray-600">
              <label v-for="tech in technologies" :key="tech.id" class="flex items-center space-x-2 text-sm text-gray-700 dark:text-gray-300 cursor-pointer hover:text-white transition-colors">
                <input type="checkbox" :value="tech.id" v-model="projectForm.technologies" class="rounded text-blue-500 focus:ring-blue-500 bg-gray-100 dark:bg-gray-700 border-gray-300 dark:border-gray-600">
                <span>{{ tech.nom }}</span>
              </label>
            </div>
            <p v-if="technologies.length === 0" class="text-xs text-yellow-500 mt-1">Aucune technologie trouvée. Ajoutez-en d'abord dans la section Technologies en bas.</p>
          </div>
          
          <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
            <div>
              <label class="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-2">Lien GitHub</label>
              <input
                v-model="projectForm.github_link"
                type="url"
                class="w-full px-3 py-2 text-sm bg-gray-100 dark:bg-gray-700 border border-gray-300 dark:border-gray-600 rounded-xl focus:outline-none focus:ring-2 focus:ring-emerald-500 text-white"
                placeholder="https://github.com/..."
              />
            </div>
            <div>
              <label class="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-2">Lien Demo</label>
              <input
                v-model="projectForm.demo_link"
                type="url"
                class="w-full px-3 py-2 text-sm bg-gray-100 dark:bg-gray-700 border border-gray-300 dark:border-gray-600 rounded-xl focus:outline-none focus:ring-2 focus:ring-emerald-500 text-white"
                placeholder="https://demo.exemple.com"
              />
            </div>
          </div>
          
          
          <div class="flex flex-wrap gap-3">
            <button
              type="submit"
              :disabled="loading"
              class="bg-emerald-600 hover:bg-emerald-700 text-white py-2 px-5 rounded-xl text-sm disabled:opacity-50"
            >
              <span v-if="!loading">{{ editingProject ? 'Modifier' : 'Déposer' }}</span>
              <span v-else>{{ editingProject ? 'Modification...' : 'Création...' }}</span>
            </button>
            <button
              type="button"
              @click="cancelEdit"
              class="bg-gray-600 hover:bg-gray-100 dark:bg-gray-700 text-white py-2 px-5 rounded-xl text-sm"
            >
              Annuler
            </button>
          </div>
        </form>
      </div>
      <!-- Section Projets -->
      <div v-if="isLoggedIn" class="mt-12 bg-gray-200 dark:bg-gray-800/30 rounded-3xl p-8 border border-white/5">
        <div class="flex flex-col md:flex-row justify-between items-center mb-8 gap-4">
          <h3 class="text-2xl font-black text-white tracking-tight flex items-center">
            <span class="w-2 h-8 bg-emerald-500 rounded-full mr-4"></span>
            Projets 
            <span class="ml-3 text-sm font-medium text-gray-500 uppercase tracking-widest">({{ projects.length }})</span>
          </h3>
          <button
            @click="showProjects = !showProjects"
            class="px-6 py-2 rounded-full border border-gray-300 dark:border-gray-700 hover:border-emerald-500 text-gray-500 dark:text-gray-400 hover:text-emerald-500 transition-all text-sm font-bold"
          >
            {{ showProjects ? 'Masquer les projets' : 'Afficher les projets' }}
          </button>
        </div>

        <div v-if="showProjects" class="flex overflow-x-auto gap-8 pb-10 px-2 scroll-smooth custom-carousel">
          <div 
            v-for="project in projects" 
            :key="project.id" 
            class="flex-none w-80 h-[450px] relative rounded-[2rem] overflow-hidden group shadow-2xl transition-all duration-500 hover:scale-[1.02] hover:shadow-emerald-500/10 border border-white/5 bg-gray-200 dark:bg-gray-800"
          >
            <!-- Image de fond -->
            <img 
              v-if="project.image_url"
              :src="project.image_url" 
              :alt="project.project_name" 
              class="absolute inset-0 w-full h-full object-cover transition-transform duration-1000 group-hover:scale-110 opacity-60 group-hover:opacity-80"
              @error="(e) => e.target.style.display = 'none'"
            >
            
            <!-- Overlay dégradé -->
            <div class="absolute inset-0 bg-gradient-to-t from-gray-950 via-gray-950/40 to-transparent"></div>
            
            <!-- Contenu -->
            <div class="absolute inset-x-0 bottom-0 p-8 pt-20">
              <div class="relative overflow-hidden mb-3">
                <h4 class="text-2xl font-black text-white shrink-0 drop-shadow-lg transition-all duration-500 line-clamp-2 break-all">
                  {{ project.project_name }}
                </h4>
              </div>
              <p class="text-sm text-gray-500 dark:text-gray-400 line-clamp-2 group-hover:line-clamp-none transition-all duration-500 mb-6 font-medium">
                {{ project.project_description }}
              </p>
              
              <!-- Actions -->
              <div class="flex gap-3 translate-y-6 opacity-0 group-hover:translate-y-0 group-hover:opacity-100 transition-all duration-500 ease-out">
                <button 
                  @click="editProject(project)"
                  class="flex-1 bg-white text-gray-900 py-3 rounded-2xl font-bold text-sm transition-all hover:bg-emerald-500 hover:text-white shadow-xl active:scale-95"
                >
                  Détails / Éditer
                </button>
                <button 
                  @click="askDeleteProject(project.id)"
                  class="bg-red-500/10 hover:bg-red-500 text-red-500 hover:text-white p-3 rounded-2xl transition-all border border-red-500/20 shadow-xl active:scale-95"
                  title="Supprimer"
                >
                  <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16" />
                  </svg>
                </button>
              </div>
            </div>
          </div>
          
          <div v-if="projects.length === 0" class="flex-none w-80 h-[450px] rounded-[2rem] border-2 border-dashed border-gray-300 dark:border-gray-700/50 flex flex-col items-center justify-center text-gray-500 italic bg-gray-200 dark:bg-gray-800/10">
            <Rocket class="mb-6 opacity-30 grayscale" :size="64" />
            <span class="font-bold tracking-widest text-xs uppercase">Aucun projet</span>
          </div>
        </div>
      </div>

      <!-- Section Technologies -->
      <div v-if="isLoggedIn" class="mt-8 bg-gray-200 dark:bg-gray-800/30 rounded-3xl p-8 border border-white/5 mb-12">
        <div class="flex flex-col md:flex-row justify-between items-center mb-8 gap-4">
          <h3 class="text-2xl font-black text-white tracking-tight flex items-center">
            <span class="w-2 h-8 bg-blue-500 rounded-full mr-4"></span>
            Technologies
            <span class="ml-3 text-sm font-medium text-gray-500 uppercase tracking-widest">({{ technologies.length }})</span>
          </h3>
        </div>
        
        <form @submit.prevent="createTechnology" class="flex gap-4 mb-8 max-w-xl">
          <input 
            v-model="newTechName" 
            type="text" 
            required 
            placeholder="Nouvelle technologie (ex: Vue.js)" 
            class="flex-1 px-4 py-3 bg-gray-100 dark:bg-gray-700 border border-gray-300 dark:border-gray-600 rounded-xl focus:outline-none focus:ring-2 focus:ring-blue-500 text-white shadow-inner"
          />
          <button type="submit" :disabled="loading" class="bg-blue-600 hover:bg-blue-700 text-white px-6 py-3 rounded-xl transition-colors font-semibold shadow-lg shadow-blue-500/20 disabled:opacity-50">Ajouter</button>
        </form>

        <div class="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-4 lg:grid-cols-6 gap-4">
          <div v-for="tech in technologies" :key="tech.id" class="bg-gray-100 dark:bg-gray-700/50 rounded-2xl p-4 flex justify-between items-center group border border-white/5 hover:border-blue-500/50 transition-all hover:bg-gray-100 dark:bg-gray-700 shadow-md">
            <span class="text-sm font-semibold text-gray-800 dark:text-gray-200 truncate">{{ tech.nom }}</span>
            <button @click="askDeleteTechnology(tech.id)" class="text-gray-500 dark:text-gray-400 hover:text-red-500 opacity-0 group-hover:opacity-100 transition-all hover:scale-110 focus:opacity-100" title="Supprimer">
              <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16" />
              </svg>
            </button>
          </div>
          <div v-if="technologies.length === 0" class="col-span-full py-8 text-center text-gray-500 italic">
            Aucune technologie enregistrée.
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { ref, computed, onMounted } from 'vue'
import { use } from 'echarts/core'
import { CanvasRenderer } from 'echarts/renderers'
import { PieChart, BarChart, LineChart } from 'echarts/charts'
import {
  TitleComponent,
  TooltipComponent,
  LegendComponent,
  GridComponent
} from 'echarts/components'
import VChart from 'vue-echarts'
import api from '../services/api.js'
import { parseProjectsResponse } from '../utils/projects.js'
import { Plus, RefreshCw, BookOpen, Rocket } from 'lucide-vue-next'

// Enregistrer les composants ECharts
use([
  CanvasRenderer,
  PieChart,
  BarChart,
  LineChart,
  TitleComponent,
  TooltipComponent,
  LegendComponent,
  GridComponent
])

export default {
  name: 'Admin',
  components: {
    VChart,
    Plus,
    RefreshCw,
    BookOpen,
    Rocket
  },
  setup() {
    const isLoggedIn = ref(false)
    const loading = ref(false)
    const error = ref('')
    const showProjects = ref(false)
    const showCreateForm = ref(false)
    const showPassword = ref(false)
    const projects = ref([])
    const technologies = ref([])
    const newTechName = ref('')
    const localPreview = ref('')
    const editingProject = ref(null)

    const toast = ref({ show: false, message: '', type: 'success' })
    const showDeleteConfirm = ref(false)
    const itemToDelete = ref(null)
    const deleteType = ref('')

    const showToast = (message, type = 'success') => {
      toast.value = { show: true, message, type }
      setTimeout(() => { toast.value.show = false }, 3000)
    }

    const loginForm = ref({
      username: '',
      password: ''
    })

    const projectForm = ref({
      project_name: '',
      project_description: '',
      project_image: '',
      technologies: [],
      github_link: '',
      demo_link: ''
    })

    const publishedProjects = computed(() => {
      return projects.value.length
    })

    // Statistiques du dashboard
    const projectsThisMonth = computed(() => {
      const now = new Date()
      const thisMonth = now.getMonth()
      const thisYear = now.getFullYear()
      
      return projects.value.filter(p => {
        const createdDate = new Date(p.date_creation)
        return createdDate.getMonth() === thisMonth && createdDate.getFullYear() === thisYear
      }).length
    })

    const uniqueTechnologies = computed(() => {
      return technologies.value.length
    })

    const projectsWithGithub = computed(() => {
      return projects.value.filter(p => p.github_link && p.github_link.trim() !== '').length
    })

    const projectsWithGithubPercent = computed(() => {
      if (projects.value.length === 0) return 0
      return Math.round((projectsWithGithub.value / projects.value.length) * 100)
    })

    const projectsWithDemo = computed(() => {
      return projects.value.filter(p => p.demo_link && p.demo_link.trim() !== '').length
    })

    const analyticsStats = ref(null)

    // Configuration graphique visiteurs
    const visitorsChartOption = computed(() => {
      const data = analyticsStats.value?.visitors_timeline || []
      const dates = data.map(item => {
        const d = new Date(item.date)
        return d.toLocaleDateString('fr-FR', { day: '2-digit', month: 'short' })
      })
      const visitors = data.map(item => item.visitors)

      return {
        tooltip: {
          trigger: 'axis',
          backgroundColor: 'rgba(17, 24, 39, 0.95)',
          borderColor: '#10b981',
          borderWidth: 1,
          textStyle: { color: '#fff' }
        },
        grid: { left: '3%', right: '4%', bottom: '3%', top: '10%', containLabel: true },
        xAxis: {
          type: 'category',
          data: dates,
          axisLabel: { color: '#9ca3af', rotate: 45 },
          axisLine: { lineStyle: { color: '#374151' } }
        },
        yAxis: {
          type: 'value',
          axisLabel: { color: '#9ca3af' },
          axisLine: { lineStyle: { color: '#374151' } },
          splitLine: { lineStyle: { color: '#374151', type: 'dashed' } }
        },
        series: [
          {
            name: 'Visiteurs uniques',
            type: 'line',
            smooth: true,
            data: visitors,
            itemStyle: { color: '#10b981' },
            areaStyle: {
              color: {
                type: 'linear', x: 0, y: 0, x2: 0, y2: 1,
                colorStops: [
                  { offset: 0, color: 'rgba(16, 185, 129, 0.5)' },
                  { offset: 1, color: 'rgba(16, 185, 129, 0.0)' }
                ]
              }
            }
          }
        ]
      }
    })

    // Configuration graphique top projets
    const topProjectsChartOption = computed(() => {
      const data = analyticsStats.value?.top_projects || []
      const names = data.map(item => item.project_name)
      const views = data.map(item => item.views)

      return {
        tooltip: {
          trigger: 'axis',
          axisPointer: { type: 'shadow' },
          backgroundColor: 'rgba(17, 24, 39, 0.95)',
          borderColor: '#3b82f6',
          borderWidth: 1,
          textStyle: { color: '#fff' }
        },
        grid: { left: '3%', right: '4%', bottom: '3%', top: '10%', containLabel: true },
        xAxis: {
          type: 'value',
          axisLabel: { color: '#9ca3af' },
          axisLine: { lineStyle: { color: '#374151' } },
          splitLine: { lineStyle: { color: '#374151', type: 'dashed' } }
        },
        yAxis: {
          type: 'category',
          data: names,
          axisLabel: { color: '#9ca3af' },
          axisLine: { lineStyle: { color: '#374151' } }
        },
        series: [
          {
            name: 'Vues',
            type: 'bar',
            data: views,
            itemStyle: {
              color: {
                type: 'linear', x: 0, y: 0, x2: 1, y2: 0,
                colorStops: [
                  { offset: 0, color: '#3b82f6' },
                  { offset: 1, color: '#1d4ed8' }
                ]
              },
              borderRadius: [0, 8, 8, 0]
            }
          }
        ]
      }
    })

    const imagePreviewUrl = computed(() => {
      if (localPreview.value) return localPreview.value
      if (typeof projectForm.value.project_image === 'string') return projectForm.value.project_image
      return null
    })

    const login = async () => {
      loading.value = true
      error.value = ''
      
      try {
        const response = await api.adminLogin(loginForm.value)
        console.log('Réponse authentification:', response.data)
        
        if (response.data.success) {
          isLoggedIn.value = true
          if (response.data.token) {
            localStorage.setItem('authToken', response.data.token)
          }
          await loadProjects()
          await loadTechnologies()
          await loadAnalytics()
        } else {
          error.value = response.data.message || 'Erreur de connexion'
        }
      } catch (err) {
        console.error('Erreur authentification:', err)
        error.value = err.response?.data?.message || 'Erreur de connexion'
      } finally {
        loading.value = false
      }
    }

    const loadAnalytics = async () => {
      try {
        const response = await api.getAnalyticsStats('30d')
        analyticsStats.value = response.data
      } catch (err) {
        console.error('Erreur chargement analytics:', err)
      }
    }

    const logout = () => {
      localStorage.removeItem('authToken')
      isLoggedIn.value = false
      projects.value = []
      technologies.value = []
    }

    const loadProjects = async () => {
      try {
        const response = await api.getProjects()
        projects.value = parseProjectsResponse(response.data)
      } catch (err) {
        console.error('Erreur chargement projets:', err)
      }
    }

    const loadTechnologies = async () => {
      try {
        const response = await api.getTechnologies()
        technologies.value = response.data.results || response.data
      } catch (err) {
        console.error('Erreur chargement technologies:', err)
      }
    }


    const handleFileChange = (e) => {
      const file = e.target.files[0]
      if (file) {
        projectForm.value.project_image = file
        localPreview.value = URL.createObjectURL(file)
      }
    }


    const openCreateForm = () => {
      editingProject.value = null
      projectForm.value = {
        project_name: '',
        project_description: '',
        project_image: '',
        technologies: [],
        github_link: '',
        demo_link: ''
      }
      localPreview.value = ''
      showCreateForm.value = true
    }

    const cancelEdit = () => {
      showCreateForm.value = false
      editingProject.value = null
      projectForm.value = {
        project_name: '',
        project_description: '',
        project_image: '',
        technologies: [],
        github_link: '',
        demo_link: ''
      }
      localPreview.value = ''
    }

    const createProject = async () => {
      loading.value = true
      
      try {
        if (editingProject.value) {
          await api.updateProject(editingProject.value.id, projectForm.value)
          showToast('Projet modifié avec succès !', 'success')
        } else {
          await api.createProject(projectForm.value)
          showToast('Projet créé avec succès !', 'success')
        }
        
        cancelEdit()
        await loadProjects()
      } catch (err) {
        console.error('Erreur sauvegarde projet:', err)
        console.error('Détails erreur:', err.response?.data)
        showToast(`Erreur: ${err.response?.data?.detail || err.message || 'Erreur lors de la sauvegarde du projet'}`, 'error')
      } finally {
        loading.value = false
      }
    }

    const editProject = (project) => {
      editingProject.value = project
      projectForm.value = {
        project_name: project.project_name,
        project_description: project.project_description,
        project_image: project.image_url || '',
        technologies: project.technologies_details ? project.technologies_details.map(t => t.id) : [],
        github_link: project.github_link || '',
        demo_link: project.demo_link || ''
      }
      localPreview.value = project.image_url || ''
      showCreateForm.value = true
    }

    const askDeleteProject = (id) => {
      deleteType.value = 'project'
      itemToDelete.value = id
      showDeleteConfirm.value = true
    }

    const askDeleteTechnology = (id) => {
      deleteType.value = 'technology'
      itemToDelete.value = id
      showDeleteConfirm.value = true
    }

    const confirmDelete = async () => {
      showDeleteConfirm.value = false
      if (deleteType.value === 'project') {
        try {
          await api.deleteProject(itemToDelete.value)
          showToast('Projet supprimé avec succès !', 'success')
          await loadProjects()
        } catch (err) {
          console.error('Erreur suppression:', err)
          showToast('Erreur lors de la suppression', 'error')
        }
      } else if (deleteType.value === 'technology') {
        try {
          await api.deleteTechnology(itemToDelete.value)
          showToast('Technologie supprimée avec succès !', 'success')
          await loadTechnologies()
        } catch (err) {
          console.error('Erreur suppression tech:', err)
          showToast('Erreur lors de la suppression', 'error')
        }
      }
    }

    const createTechnology = async () => {
      if (!newTechName.value.trim()) return
      loading.value = true
      try {
        await api.createTechnology({ nom: newTechName.value })
        showToast('Technologie ajoutée avec succès !', 'success')
        newTechName.value = ''
        await loadTechnologies()
      } catch (err) {
        console.error('Erreur ajout technologie:', err)
        showToast('Erreur lors de l\'ajout de la technologie', 'error')
      } finally {
        loading.value = false
      }
    }

    const refreshData = () => {
      loadProjects()
    }

    const goToPortfolio = () => {
      window.open('/', '_blank')
    }

    const goToApiDocs = () => {
      window.open('https://portefolio-backend-v0e0.onrender.com/docs/', '_blank')
    }

    onMounted(() => {
      // Vérifier si un token existe déjà
      const token = localStorage.getItem('authToken')
      if (token) {
        isLoggedIn.value = true
        loadProjects()
        loadTechnologies()
        loadAnalytics()
      }
    })

    return {
      isLoggedIn,
      loading,
      error,
      showProjects,
      showPassword,
      showCreateForm,
      editingProject,
      projects,
      technologies,
      newTechName,
      toast,
      showDeleteConfirm,
      loginForm,
      projectForm,
      publishedProjects,
      imagePreviewUrl,
      handleFileChange,
      login,
      openCreateForm,
      cancelEdit,
      createProject,
      editProject,
      askDeleteProject,
      askDeleteTechnology,
      confirmDelete,
      createTechnology,
      refreshData,
      goToPortfolio,
      goToApiDocs,
      logout,
      // Dashboard stats
      projectsThisMonth,
      uniqueTechnologies,
      projectsWithGithub,
      projectsWithGithubPercent,
      projectsWithDemo,
      // ECharts options
      visitorsChartOption,
      topProjectsChartOption,
      analyticsStats
    }
  }
}
</script>

<style scoped>
.custom-carousel {
  scrollbar-width: thin;
  scrollbar-color: #10b981 #1f2937;
}

.custom-carousel::-webkit-scrollbar {
  height: 6px;
}

.custom-carousel::-webkit-scrollbar-track {
  background: #1f2937;
  border-radius: 10px;
}

.custom-carousel::-webkit-scrollbar-thumb {
  background-color: #10b981;
  border-radius: 10px;
}

/* Line-clamp utility if not available through Tailwind */
.line-clamp-2 {
  display: -webkit-box;
  -webkit-line-clamp: 2;
  line-clamp: 2;
  -webkit-box-orient: vertical;  
  overflow: hidden;
}
</style>

