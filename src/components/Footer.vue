<template>
  <footer class="bg-white dark:bg-dark-jungle border-t border-gray-200 dark:border-gray-800 mt-16">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12">
      <div class="grid md:grid-cols-3 gap-8">
        <!-- Informations personnelles -->
        <div>
          <h3 class="text-xl font-semibold text-emerald mb-4">{{ $t('footer.contact') }}</h3>
          <div class="space-y-3">
            <div class="flex items-center space-x-3">
              <span class="text-emerald"><Mail :size="20" /></span>
              <a href="mailto:mokumabrady13@gmail.com" class="text-gray-600 dark:text-gray-custom hover:text-emerald transition-colors">
                mokumabrady13@gmail.com
              </a>
            </div>
            <div class="flex items-center space-x-3">
              <span class="text-emerald"><Smartphone :size="20" /></span>
              <span class="text-gray-600 dark:text-gray-custom">074 14 59 49 / 062 44 50 33</span>
            </div>
            <div class="flex items-center space-x-3">
              <span class="text-emerald"><MapPin :size="20" /></span>
              <span class="text-gray-600 dark:text-gray-custom">Libreville, Gabon</span>
            </div>
          </div>
        </div>

        <!-- Réseaux sociaux -->
        <div>
          <h3 class="text-xl font-semibold text-emerald mb-4">{{ $t('footer.networks') }}</h3>
          <div class="flex space-x-4">
            <a 
              href="https://github.com/bradyFrasnel" 
              target="_blank"
              class="w-10 h-10 bg-gray-200 dark:bg-gray-800 text-white rounded-lg flex items-center justify-center hover:bg-emerald transition-colors"
              title="GitHub"
            >
              <span class="text-lg flex justify-center"><Github :size="24" /></span>
            </a>
            <a 
              href="https://www.linkedin.com/in/brady-mokuma-9745813a8?utm_source=share_via&utm_content=profile&utm_medium=member_ios" 
              target="_blank"
              class="w-10 h-10 bg-blue-600 text-white rounded-lg flex items-center justify-center hover:bg-blue-700 transition-colors"
              title="LinkedIn"
            >
              <span class="text-lg flex justify-center"><Linkedin :size="24" /></span>
            </a>
            <a 
              href="https://wa.me/24174145949" 
              target="_blank"
              class="w-10 h-10 bg-green-600 text-white rounded-lg flex items-center justify-center hover:bg-green-700 transition-colors"
              title="WhatsApp"
            >
              <span class="text-lg flex justify-center"><MessageCircle :size="24" /></span>
            </a>
          </div>
        </div>

        <!-- Informations légales -->
        <div>
          <h3 class="text-xl font-semibold text-emerald mb-4">{{ $t('footer.info') }}</h3>
          <div class="space-y-2 text-gray-600 dark:text-gray-custom text-sm">
            <p>{{ $t('footer.dev_role') }}</p>
            <p>{{ $t('footer.availability') }}</p>
            <div class="pt-4">
              <p class="text-xs text-gray-500">{{ $t('footer.copyright') }}</p>
            </div>
          </div>
        </div>
      </div>

      <!-- mon Gabon-->
      <div class="mt-12 pt-8 border-t border-gray-200 dark:border-gray-800 text-center">
        <p class="text-lg md:text-xl font-medium italic text-emerald">
          C'est enfin notre essor vers la félicité !!
        </p>
      </div>
    </div>
  </footer>
</template>

<script setup>
import { Mail, Smartphone, MapPin, Github, Linkedin, MessageCircle } from 'lucide-vue-next'
</script>
