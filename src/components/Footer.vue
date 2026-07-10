<template>
  <footer class="bg-dark-jungle border-t border-gray-800 mt-16">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12">
      <div class="grid md:grid-cols-3 gap-8">
        <!-- Informations personnelles -->
        <div>
          <h3 class="text-xl font-semibold text-emerald mb-4">Contact</h3>
          <div class="space-y-3">
            <div class="flex items-center space-x-3">
              <span class="text-emerald">📧</span>
              <a href="mailto:mokumabrady13@gmail.com" class="text-gray-custom hover:text-emerald transition-colors">
                mokumabrady13@gmail.com
              </a>
            </div>
            <div class="flex items-center space-x-3">
              <span class="text-emerald">📱</span>
              <span class="text-gray-custom">074 14 59 49 / 062 44 50 33</span>
            </div>
            <div class="flex items-center space-x-3">
              <span class="text-emerald">📍</span>
              <span class="text-gray-custom">Libreville, Gabon</span>
            </div>
          </div>
        </div>

        <!-- Réseaux sociaux -->
        <div>
          <h3 class="text-xl font-semibold text-emerald mb-4">Réseaux</h3>
          <div class="flex space-x-4">
            <a 
              href="https://github.com" 
              target="_blank"
              class="w-10 h-10 bg-gray-800 text-white rounded-lg flex items-center justify-center hover:bg-emerald transition-colors"
              title="GitHub"
            >
              <span class="text-lg">🐙</span>
            </a>
            <a 
              href="https://linkedin.com" 
              target="_blank"
              class="w-10 h-10 bg-blue-600 text-white rounded-lg flex items-center justify-center hover:bg-blue-700 transition-colors"
              title="LinkedIn"
            >
              <span class="text-lg">💼</span>
            </a>
            <a 
              href="https://twitter.com" 
              target="_blank"
              class="w-10 h-10 bg-sky-500 text-white rounded-lg flex items-center justify-center hover:bg-sky-600 transition-colors"
              title="Twitter"
            >
              <span class="text-lg">🐦</span>
            </a>
          </div>
        </div>

        <!-- Informations légales -->
        <div>
          <h3 class="text-xl font-semibold text-emerald mb-4">Informations</h3>
          <div class="space-y-2 text-gray-custom text-sm">
            <p>Développeur Fullstack Junior</p>
            <p>Spécialisé Vue.js & Django</p>
            <p>Disponible pour missions freelance</p>
            <div class="pt-4">
              <p class="text-xs text-gray-500">© 2024 Mon Portfolio. Tous droits réservés.</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </footer>
</template>

<script setup>
</script>
