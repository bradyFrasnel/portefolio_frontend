<template>
  <div class="min-h-screen bg-gray-50 dark:bg-obsidian text-gray-900 dark:text-off-white">
    <!-- Navigation -->
    <header class="fixed top-0 w-full bg-white dark:bg-dark-jungle/95 backdrop-blur-sm border-b border-gray-200 dark:border-gray-800 z-50">
      <nav class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="flex justify-between items-center h-16">
          <div class="text-2xl font-bold text-emerald">Brady Portfolio</div>
          <div class="hidden md:flex space-x-8">
            <button @click="scrollToSection('hero')" class="text-gray-600 dark:text-gray-custom hover:text-emerald transition-colors">{{ $t('nav.home') }}</button>
            <button @click="scrollToSection('skills')" class="text-gray-600 dark:text-gray-custom hover:text-emerald transition-colors">{{ $t('nav.skills') }}</button>
            <button @click="scrollToSection('portfolio')" class="text-gray-600 dark:text-gray-custom hover:text-emerald transition-colors">{{ $t('nav.portfolio') }}</button>
            <button @click="scrollToSection('services')" class="text-gray-600 dark:text-gray-custom hover:text-emerald transition-colors">{{ $t('nav.services') }}</button>
            <button @click="scrollToSection('contact')" class="text-gray-600 dark:text-gray-custom hover:text-emerald transition-colors">{{ $t('nav.contact') }}</button>
            <button @click="scrollToSection('identifiants')" class="text-gray-600 dark:text-gray-custom hover:text-emerald transition-colors">{{ $t('nav.identifiants') }}</button>
            <router-link to="/admin" class="text-gray-600 dark:text-gray-custom hover:text-emerald transition-colors">{{ $t('nav.admin') }}</router-link>
          </div>
          <div class="flex items-center space-x-4">
            <button 
              @click="toggleLocale" 
              class="px-2 py-1 rounded-lg bg-gray-200 dark:bg-gray-800 hover:bg-gray-100 dark:bg-gray-700 transition-colors font-bold text-sm uppercase"
            >
              {{ currentLocale === 'fr' ? 'EN' : 'FR' }}
            </button>
            <button 
              @click="toggleDarkMode" 
              class="p-2 rounded-lg bg-gray-200 dark:bg-gray-800 hover:bg-gray-100 dark:bg-gray-700 transition-colors flex items-center justify-center"
            >
              <Moon v-if="isDarkMode" :size="20" />
              <Sun v-else :size="20" />
            </button>
            <button 
              @click="toggleMobileMenu" 
              class="md:hidden p-2 rounded-lg bg-gray-200 dark:bg-gray-800 hover:bg-gray-100 dark:bg-gray-700 transition-colors flex items-center justify-center"
            >
              <X v-if="mobileMenuOpen" :size="24" />
              <Menu v-else :size="24" />
            </button>
          </div>
        </div>
        <div v-show="mobileMenuOpen" class="md:hidden pb-4">
          <div class="flex flex-col space-y-4">
            <button @click="scrollToSection('hero')" class="text-gray-600 dark:text-gray-custom hover:text-emerald transition-colors py-2">{{ $t('nav.home') }}</button>
            <button @click="scrollToSection('skills')" class="text-gray-600 dark:text-gray-custom hover:text-emerald transition-colors py-2">{{ $t('nav.skills') }}</button>
            <button @click="scrollToSection('portfolio')" class="text-gray-600 dark:text-gray-custom hover:text-emerald transition-colors py-2">{{ $t('nav.portfolio') }}</button>
            <button @click="scrollToSection('services')" class="text-gray-600 dark:text-gray-custom hover:text-emerald transition-colors py-2">{{ $t('nav.services') }}</button>
            <button @click="scrollToSection('contact')" class="text-gray-600 dark:text-gray-custom hover:text-emerald transition-colors py-2">{{ $t('nav.contact') }}</button>
            <button @click="scrollToSection('identifiants')" class="text-gray-600 dark:text-gray-custom hover:text-emerald transition-colors py-2">{{ $t('nav.identifiants') }}</button>
            <router-link to="/admin" class="text-gray-600 dark:text-gray-custom hover:text-emerald transition-colors py-2">{{ $t('nav.admin') }}</router-link>
          </div>
        </div>
      </nav>
    </header>

    <!-- Hero Section -->
    <section id="hero" class="min-h-screen flex items-center justify-center px-4 pt-16">
      <div class="text-center max-w-4xl">
        <h1 class="text-4xl sm:text-5xl md:text-6xl lg:text-7xl font-bold mb-4 sm:mb-6">
          <span class="text-emerald">{{ $t('hero.title_1') }}</span><br>
          <span class="text-gray-900 dark:text-off-white">{{ $t('hero.title_2') }}</span>
        </h1>
        <p class="text-base sm:text-lg md:text-xl lg:text-2xl text-gray-600 dark:text-gray-custom mb-6 sm:mb-8">
          {{ $t('hero.subtitle') }}
        </p>
        <div class="flex flex-col sm:flex-row gap-3 sm:gap-4 justify-center">
          <button 
            @click="scrollToSection('portfolio')"
            class="bg-emerald text-obsidian px-6 sm:px-8 py-2 sm:py-3 text-sm sm:text-base rounded-lg hover:bg-neon-lime transition-all transform hover:scale-105 font-semibold"
          >
            {{ $t('hero.btn_portfolio') }}
          </button>
          <button 
            @click="scrollToSection('contact')"
            class="border border-emerald text-emerald px-6 sm:px-8 py-2 sm:py-3 text-sm sm:text-base rounded-lg hover:bg-emerald hover:text-obsidian transition-all font-semibold"
          >
            {{ $t('hero.btn_contact') }}
          </button>
        </div>
        
        <!-- Technologies Stack -->
        <div class="mt-16 grid grid-cols-3 sm:grid-cols-6 gap-4 place-items-center">
          <div data-aos="fade-up" data-aos-delay="100"><Code class="text-emerald" :size="32" /></div>
          <div data-aos="fade-up" data-aos-delay="200"><Target class="text-emerald" :size="32" /></div>
          <div data-aos="fade-up" data-aos-delay="300"><Atom class="text-emerald" :size="32" /></div>
          <div data-aos="fade-up" data-aos-delay="400"><Palette class="text-emerald" :size="32" /></div>
          <div data-aos="fade-up" data-aos-delay="500"><Database class="text-emerald" :size="32" /></div>
          <div data-aos="fade-up" data-aos-delay="600"><Rocket class="text-emerald" :size="32" /></div>
        </div>
      </div>
    </section>

    <!-- Compétences Section -->
    <section id="skills" class="py-20 px-4 bg-gray-50 dark:bg-obsidian">
      <div class="max-w-7xl mx-auto">
        <div class="text-center mb-16">
          <h2 class="text-4xl md:text-5xl font-bold text-gray-900 dark:text-off-white mb-6">{{ $t('skills.title') }}</h2>
          <p class="text-xl text-gray-600 dark:text-gray-custom">{{ $t('skills.subtitle') }}</p>
        </div>
        
        <div v-if="technologies.length === 0" class="text-center py-8">
          <p class="text-gray-600 dark:text-gray-custom">{{ $t('skills.empty') }}</p>
        </div>
        <div v-else class="flex flex-wrap justify-center gap-6 md:gap-8">
          <div 
            v-for="tech in technologies" 
            :key="tech.id"
            class="flex flex-col items-center justify-center p-6 bg-white dark:bg-dark-jungle rounded-2xl border border-gray-200 dark:border-gray-800 hover:border-emerald hover:shadow-[0_0_15px_rgba(16,185,129,0.2)] transition-all w-32 sm:w-40"
            data-aos="zoom-in"
          >
            <div class="h-16 w-16 mb-4 flex items-center justify-center">
              <img v-if="tech.image_url" :src="tech.image_url" :alt="tech.nom" class="max-h-full max-w-full object-contain">
              <Code v-else class="text-emerald" :size="40" />
            </div>
            <span class="text-sm sm:text-base font-semibold text-gray-800 dark:text-gray-200 text-center">{{ tech.nom }}</span>
          </div>
        </div>
      </div>
    </section>

    <!-- Portfolio Section -->
    <section id="portfolio" class="py-20 px-4">
      <div class="max-w-7xl mx-auto">
        <div class="text-center mb-8 sm:mb-16 px-2 sm:px-0">
          <h2 class="text-3xl sm:text-4xl md:text-5xl font-bold text-gray-900 dark:text-off-white mb-4 sm:mb-6">{{ $t('portfolio.title') }}</h2>
          <p class="text-base sm:text-xl text-gray-600 dark:text-gray-custom">{{ $t('portfolio.subtitle') }}</p>
        </div>

        <!-- État : Chargement -->
        <div v-if="projectsLoading" class="flex flex-col items-center justify-center py-20 gap-6">
          <div class="loader-ring"></div>
          <p class="text-gray-600 dark:text-gray-custom text-sm animate-pulse">
            {{ loadingMessage }}
          </p>
          <p class="text-xs text-gray-500">{{ $t('portfolio.loading_delay') }}</p>
        </div>

        <!-- État : Erreur -->
        <div v-else-if="projectsError" class="text-center py-12 flex flex-col items-center">
          <Frown class="text-gray-500 mb-4" :size="48" />
          <p class="text-red-400 mb-4">{{ projectsError }}</p>
          <button
            @click="loadData"
            class="bg-emerald text-obsidian px-6 py-2 rounded-lg hover:bg-neon-lime transition-all font-semibold"
          >
            {{ $t('portfolio.retry') }}
          </button>
        </div>

        <!-- État : Aucun projet -->
        <div v-else-if="filteredProjects.length === 0" class="text-center py-12 flex flex-col items-center">
          <Rocket class="text-gray-500 mb-4" :size="48" />
          <p class="text-gray-600 dark:text-gray-custom">{{ $t('portfolio.empty') }}</p>
        </div>

        <!-- Grille de projets -->
        <div v-else class="flex flex-wrap justify-center gap-8">
          <div 
            v-for="project in filteredProjects" 
            :key="project.id"
            class="project-card bg-white dark:bg-dark-jungle p-6 rounded-xl border border-gray-200 dark:border-gray-800 hover:border-emerald transition-all cursor-pointer w-full md:w-[calc(50%-1rem)] lg:w-[calc(33.333%-1.5rem)] max-w-sm flex-grow-0"
            @click="showProjectDetail(project)"
            data-aos="fade-up"
          >
            <!-- Miniature image -->
            <div class="w-full h-32 sm:h-40 md:h-48 rounded-lg mb-4 overflow-hidden bg-gray-200 dark:bg-gray-800 relative">
              <img 
                v-if="project.image_url"
                :src="project.image_url" 
                :alt="project.project_name"
                class="w-full h-full object-cover transition-transform duration-300 group-hover:scale-105"
                @error="(e) => e.target.style.display = 'none'"
              >
              <!-- Placeholder CSS quand pas d'image (aucune dépendance externe) -->
              <div 
                v-if="!project.image_url"
                class="w-full h-full flex flex-col items-center justify-center gap-2 project-placeholder"
              >
                <Monitor :size="48" class="opacity-60 text-gray-500 dark:text-gray-400" />
                <span class="text-xs text-gray-500 font-medium uppercase tracking-widest">{{ project.project_name.charAt(0) }}</span>
              </div>
            </div>
            <h3 class="text-xl font-semibold mb-2 text-gray-900 dark:text-off-white">{{ project.project_name }}</h3>
            <p class="text-gray-600 dark:text-gray-custom mb-4 line-clamp-2">{{ project.project_description }}</p>
            <div class="flex flex-wrap gap-2 mb-4">
              <span v-for="tech in project.technologies_details" :key="tech.id"
                    class="px-3 py-1 bg-emerald/20 text-emerald rounded-full text-sm">
                {{ tech.nom }}
              </span>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Services Section -->
    <section id="services" class="py-20 px-4 bg-white dark:bg-dark-jungle">
      <div class="max-w-7xl mx-auto">
        <div class="text-center mb-16">
          <h2 class="text-4xl md:text-5xl font-bold text-gray-900 dark:text-off-white mb-6">{{ $t('services.title') }}</h2>
          <p class="text-xl text-gray-600 dark:text-gray-custom">{{ $t('services.subtitle') }}</p>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-3 gap-6 md:gap-8">
          <div class="text-center p-4 sm:p-6 md:p-8 flex flex-col items-center" data-aos="fade-up" data-aos-delay="100">
            <Monitor :size="48" class="text-emerald mb-3 sm:mb-6" />
            <h3 class="text-lg sm:text-xl md:text-2xl font-semibold mb-2 sm:mb-4 text-emerald">{{ $t('services.dev_title') }}</h3>
            <p class="text-sm sm:text-base text-gray-600 dark:text-gray-custom">{{ $t('services.dev_desc') }}</p>
          </div>
          <div class="text-center p-4 sm:p-6 md:p-8 flex flex-col items-center" data-aos="fade-up" data-aos-delay="200">
            <Bot :size="48" class="text-emerald mb-3 sm:mb-6" />
            <h3 class="text-lg sm:text-xl md:text-2xl font-semibold mb-2 sm:mb-4 text-emerald">{{ $t('services.auto_title') }}</h3>
            <p class="text-sm sm:text-base text-gray-600 dark:text-gray-custom">{{ $t('services.auto_desc') }}</p>
          </div>
          <div class="text-center p-4 sm:p-6 md:p-8 flex flex-col items-center" data-aos="fade-up" data-aos-delay="300">
            <Wrench :size="48" class="text-emerald mb-3 sm:mb-6" />
            <h3 class="text-lg sm:text-xl md:text-2xl font-semibold mb-2 sm:mb-4 text-emerald">{{ $t('services.maint_title') }}</h3>
            <p class="text-sm sm:text-base text-gray-600 dark:text-gray-custom">{{ $t('services.maint_desc') }}</p>
          </div>
        </div>
      </div>
    </section>

    <!-- Contact Section -->
    <section id="contact" class="py-20 px-4">
      <div class="max-w-4xl mx-auto">
        <div class="text-center mb-16">
          <h2 class="text-4xl md:text-5xl font-bold text-gray-900 dark:text-off-white mb-6">{{ $t('contact.title') }}</h2>
          <p class="text-xl text-gray-600 dark:text-gray-custom">{{ $t('contact.subtitle') }}</p>
        </div>

        <form @submit.prevent="submitContact" class="space-y-6">
          <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
            <div>
              <label class="block text-sm font-medium text-gray-600 dark:text-gray-custom mb-2">{{ $t('contact.name') }}</label>
              <input
                v-model="contactForm.nom"
                type="text"
                required
                class="w-full px-3 sm:px-4 py-2 sm:py-3 bg-white dark:bg-dark-jungle border border-gray-200 dark:border-gray-800 rounded-lg focus:outline-none focus:ring-2 focus:ring-emerald text-gray-900 dark:text-off-white text-sm sm:text-base"
                :placeholder="$t('contact.name_ph')"
              />
            </div>
            <div>
              <label class="block text-sm font-medium text-gray-600 dark:text-gray-custom mb-2">{{ $t('contact.email') }}</label>
              <input
                v-model="contactForm.email"
                type="email"
                required
                class="w-full px-3 sm:px-4 py-2 sm:py-3 bg-white dark:bg-dark-jungle border border-gray-200 dark:border-gray-800 rounded-lg focus:outline-none focus:ring-2 focus:ring-emerald text-gray-900 dark:text-off-white text-sm sm:text-base"
                :placeholder="$t('contact.email_ph')"
              />
            </div>
            </div>
            
            <div>
              <label class="block text-sm font-medium text-gray-600 dark:text-gray-custom mb-2">{{ $t('contact.phone') }}</label>
              <input
                v-model="contactForm.telephone"
                type="tel"
                class="w-full px-3 sm:px-4 py-2 sm:py-3 bg-white dark:bg-dark-jungle border border-gray-200 dark:border-gray-800 rounded-lg focus:outline-none focus:ring-2 focus:ring-emerald text-gray-900 dark:text-off-white text-sm sm:text-base"
                :placeholder="$t('contact.phone_ph')"
              />
            </div>

            <div>
              <label class="block text-sm font-medium text-gray-600 dark:text-gray-custom mb-2">{{ $t('contact.project_type') }}</label>
            <select
              v-model="contactForm.type_projet"
              required
              class="w-full px-3 sm:px-4 py-2 sm:py-3 bg-white dark:bg-dark-jungle border border-gray-200 dark:border-gray-800 rounded-lg focus:outline-none focus:ring-2 focus:ring-emerald text-gray-900 dark:text-off-white text-sm sm:text-base"
            >
              <option value="">{{ $t('contact.select_ph') }}</option>
              <option :value="$t('contact.type_showcase')">{{ $t('contact.type_showcase') }}</option>
              <option :value="$t('contact.type_webapp')">{{ $t('contact.type_webapp') }}</option>
              <option :value="$t('contact.type_ecommerce')">{{ $t('contact.type_ecommerce') }}</option>
              <option :value="$t('contact.type_other')">{{ $t('contact.type_other') }}</option>
            </select>
          </div>

          <div>
            <label class="block text-sm font-medium text-gray-600 dark:text-gray-custom mb-2">{{ $t('contact.message') }}</label>
            <textarea
              v-model="contactForm.message"
              required
              rows="6"
              class="w-full px-3 sm:px-4 py-2 sm:py-3 bg-white dark:bg-dark-jungle border border-gray-200 dark:border-gray-800 rounded-lg focus:outline-none focus:ring-2 focus:ring-emerald text-gray-900 dark:text-off-white text-sm sm:text-base"
              :placeholder="$t('contact.message_ph')"
            ></textarea>
          </div>

          <div class="text-center">
            <button
              type="submit"
              :disabled="loading"
              class="bg-emerald text-obsidian px-6 sm:px-8 py-2 sm:py-3 text-sm sm:text-base rounded-lg hover:bg-neon-lime transition-all transform hover:scale-105 font-semibold disabled:opacity-50"
            >
              <span v-if="!loading">{{ $t('contact.btn_send') }}</span>
              <span v-else>{{ $t('contact.btn_sending') }}</span>
            </button>
          </div>
        </form>

        <div v-if="successMessage" class="mt-6 p-4 bg-emerald/20 border border-emerald rounded-lg text-emerald text-center">
          {{ successMessage }}
        </div>
      </div>
    </section>

    <!-- Identifiants Section -->
    <section id="identifiants" class="py-20 px-4 bg-white dark:bg-dark-jungle">
      <div class="max-w-7xl mx-auto">
        <div class="text-center mb-16">
          <h2 class="text-4xl md:text-5xl font-bold text-gray-900 dark:text-off-white mb-6">{{ $t('identifiants.title') }}</h2>
          <p class="text-xl text-gray-600 dark:text-gray-custom">{{ $t('identifiants.subtitle') }}</p>
        </div>

        <!-- Cartes Identifiants -->
        <div class="flex flex-wrap justify-center gap-8">
          <!-- GitHub -->
          <div class="text-center p-6 bg-gray-50 dark:bg-obsidian rounded-xl border border-gray-200 dark:border-gray-800 hover:border-emerald transition-all w-full md:w-[calc(50%-1rem)] lg:w-[calc(33.333%-1.5rem)] max-w-sm flex-grow-0" data-aos="fade-up" data-aos-delay="100">
            <img src="@/assets/icones/github.png" alt="GitHub" class="h-16 w-16 mx-auto mb-4 object-contain">
            <h3 class="text-xl font-semibold mb-3 text-emerald">GitHub</h3>
            <p class="text-gray-600 dark:text-gray-custom mb-4">{{ $t('identifiants.github_desc') }}</p>
            <a 
              href="https://github.com/bradyFrasnel" 
              target="_blank"
              class="inline-flex items-center gap-2 bg-emerald text-obsidian px-4 sm:px-6 py-2 text-sm sm:text-base rounded-lg hover:bg-neon-lime transition-all font-semibold"
            >
              <span>{{ $t('identifiants.github_btn') }}</span>
              <span>→</span>
            </a>
          </div>

          <!-- LinkedIn -->
          <div class="text-center p-6 bg-gray-50 dark:bg-obsidian rounded-xl border border-gray-200 dark:border-gray-800 hover:border-emerald transition-all w-full md:w-[calc(50%-1rem)] lg:w-[calc(33.333%-1.5rem)] max-w-sm flex-grow-0" data-aos="fade-up" data-aos-delay="200">
            <img src="@/assets/icones/linkedin.png" alt="LinkedIn" class="h-16 w-16 mx-auto mb-4 object-contain">
            <h3 class="text-xl font-semibold mb-3 text-emerald">LinkedIn</h3>
            <p class="text-gray-600 dark:text-gray-custom mb-4">{{ $t('identifiants.linkedin_desc') }}</p>
            <a 
              href="https://www.linkedin.com/in/brady-mokuma-9745813a8?utm_source=share_via&utm_content=profile&utm_medium=member_ios" 
              target="_blank"
              class="inline-flex items-center gap-2 bg-emerald text-obsidian px-4 sm:px-6 py-2 text-sm sm:text-base rounded-lg hover:bg-neon-lime transition-all font-semibold"
            >
              <span>{{ $t('identifiants.linkedin_btn') }}</span>
              <span>→</span>
            </a>
          </div>

          <!-- Email -->
          <div class="text-center p-6 bg-gray-50 dark:bg-obsidian rounded-xl border border-gray-200 dark:border-gray-800 hover:border-emerald transition-all w-full md:w-[calc(50%-1rem)] lg:w-[calc(33.333%-1.5rem)] max-w-sm flex-grow-0" data-aos="fade-up" data-aos-delay="300">
            <img src="@/assets/icones/mail.png" alt="Email" class="h-16 w-16 mx-auto mb-4 object-contain">
            <h3 class="text-xl font-semibold mb-3 text-emerald">Email</h3>
            <p class="text-gray-600 dark:text-gray-custom mb-4">{{ $t('identifiants.email_desc') }}</p>
            <a 
              href="mailto:mokumabrady13@gmail.com" 
              class="inline-flex items-center gap-2 bg-emerald text-obsidian px-4 sm:px-6 py-2 text-sm sm:text-base rounded-lg hover:bg-neon-lime transition-all font-semibold truncate"
            >
              <span class="truncate">mokumabrady13@gmail.com</span>
              <span>→</span>
            </a>
          </div>

          <!-- WhatsApp -->
          <div class="text-center p-6 bg-gray-50 dark:bg-obsidian rounded-xl border border-gray-200 dark:border-gray-800 hover:border-emerald transition-all w-full md:w-[calc(50%-1rem)] lg:w-[calc(33.333%-1.5rem)] max-w-sm flex-grow-0" data-aos="fade-up" data-aos-delay="400">
            <img src="@/assets/icones/whatsApp2.png" alt="WhatsApp" class="h-16 w-16 mx-auto mb-4 object-contain">
            <h3 class="text-xl font-semibold mb-3 text-emerald">WhatsApp</h3>
            <p class="text-gray-600 dark:text-gray-custom mb-4">{{ $t('identifiants.whatsapp_desc') }}</p>
            <a 
              href="https://wa.me/24174145949" 
              target="_blank"
              class="inline-flex items-center gap-2 bg-emerald text-obsidian px-4 sm:px-6 py-2 text-sm sm:text-base rounded-lg hover:bg-neon-lime transition-all font-semibold"
            >
              <span>{{ $t('identifiants.whatsapp_btn') }}</span>
              <span>→</span>
            </a>
          </div>
        </div>

        <!-- Informations additionnelles -->
        <div class="mt-16 text-center">
          <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
            <div class="bg-gray-50 dark:bg-obsidian p-6 rounded-xl border border-gray-200 dark:border-gray-800">
            <img src="@/assets/icones/localisation.png" alt="Localisation" class="h-8 w-8 inline-block mr-2">{{ $t('identifiants.location_title') }}
              <p class="text-gray-600 dark:text-gray-custom">{{ $t('identifiants.location_desc') }}</p>
            </div>
            <div class="bg-gray-50 dark:bg-obsidian p-6 rounded-xl border border-gray-200 dark:border-gray-800">
              <h4 class="text-lg font-semibold mb-3 text-emerald flex items-center justify-center md:justify-start gap-2"><Zap :size="20" /> {{ $t('identifiants.availability_title') }}</h4>
              <p class="text-gray-600 dark:text-gray-custom">{{ $t('identifiants.availability_desc') }}</p>
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
      <div class="bg-white dark:bg-dark-jungle rounded-xl p-4 sm:p-6 md:p-8 max-w-2xl w-full max-h-[90vh] overflow-y-auto" @click.stop>
        <div class="flex flex-col sm:flex-row sm:justify-between sm:items-start mb-4 sm:mb-6 gap-2">
          <h3 class="text-xl sm:text-2xl font-bold text-gray-900 dark:text-off-white">{{ selectedProject.project_name }}</h3>
          <button 
            @click="closeProjectDetail"
            class="self-end sm:self-auto text-gray-600 dark:text-gray-custom hover:text-gray-900 dark:text-off-white text-2xl"
          >
            ✕
          </button>
        </div>
        
        <!-- Image du projet dans la modale -->
        <div class="w-full aspect-video rounded-lg mb-6 overflow-hidden bg-gray-200 dark:bg-gray-800">
          <img 
            v-if="selectedProject.image_url"
            :src="selectedProject.image_url" 
            :alt="selectedProject.project_name"
            class="w-full h-full object-cover"
            @error="(e) => e.target.style.display = 'none'"
          >
          <!-- Placeholder CSS si pas d'image -->
          <div 
            v-if="!selectedProject.image_url"
            class="w-full h-full flex flex-col items-center justify-center gap-3 project-placeholder"
          >
            <Monitor :size="48" class="opacity-60 text-gray-500 dark:text-gray-400" />
            <span class="text-sm text-gray-500 font-medium">{{ $t('portfolio.no_image') }}</span>
          </div>
        </div>
        
        <p class="text-gray-600 dark:text-gray-custom mb-6">{{ selectedProject.project_description }}</p>
        
        <div class="flex flex-wrap gap-2 mb-6">
          <span v-for="tech in selectedProject.technologies_details" :key="tech.id"
                class="px-3 py-1 bg-emerald/20 text-emerald rounded-full text-sm">
            {{ tech.nom }}
          </span>
        </div>
        
        <div class="flex flex-col sm:flex-row gap-3 sm:gap-4">
          <a 
            v-if="selectedProject.github_link"
            :href="selectedProject.github_link"
            target="_blank"
            class="bg-emerald text-obsidian px-4 sm:px-6 py-2 text-sm sm:text-base rounded-lg hover:bg-neon-lime transition-all text-center"
          >
            {{ $t('portfolio.view_code') }}
          </a>
          <a 
            v-if="selectedProject.demo_link"
            :href="selectedProject.demo_link"
            target="_blank"
            class="border border-emerald text-emerald px-4 sm:px-6 py-2 text-sm sm:text-base rounded-lg hover:bg-emerald hover:text-obsidian transition-all text-center"
          >
            {{ $t('portfolio.view_demo') }}
          </a>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, computed } from 'vue'
import { useI18n } from 'vue-i18n'
import { Moon, Sun, Menu, X, Monitor, Bot, Wrench, Code, Target, Atom, Palette, Database, Rocket, Frown, Zap } from 'lucide-vue-next'
import { trackEvent } from '../utils/analytics.js'
import api from '../services/api.js'
import { parseProjectsResponse } from '../utils/projects.js'

const { t, locale } = useI18n()

const currentLocale = computed(() => locale.value)
const toggleLocale = () => {
  locale.value = locale.value === 'fr' ? 'en' : 'fr'
}

const isDarkMode = ref(localStorage.getItem('theme') === 'dark' || (!('theme' in localStorage) && window.matchMedia('(prefers-color-scheme: dark)').matches))
const mobileMenuOpen = ref(false)
const loading = ref(false)
const successMessage = ref('')
const selectedProject = ref(null)

const projects = ref([])
const technologies = ref([])
const projectsLoading = ref(true)
const projectsError = ref('')

// Message animé pendant le chargement (cold start Render)
const loadingMsgIndex = ref(0)
const loadingMessage = computed(() => {
  const loadingMessages = [
    t('portfolio.loading_1'),
    t('portfolio.loading_2'),
    t('portfolio.loading_3'),
    t('portfolio.loading_4'),
  ]
  return loadingMessages[loadingMsgIndex.value % loadingMessages.length]
})
let loadingTimer = null

const contactForm = ref({
  nom: '',
  email: '',
  telephone: '',
  type_projet: '',
  message: ''
})

const filteredProjects = computed(() => {
  return projects.value
})

const toggleDarkMode = () => {
  isDarkMode.value = !isDarkMode.value
  if (isDarkMode.value) {
    if (isDarkMode.value) document.documentElement.classList.add('dark'); else document.documentElement.classList.remove('dark')
    localStorage.setItem('theme', 'dark')
  } else {
    document.documentElement.classList.remove('dark')
    localStorage.setItem('theme', 'light')
  }
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

const showProjectDetail = (project) => {
  selectedProject.value = project
  trackEvent('project_detail', project.id)
}

const closeProjectDetail = () => {
  selectedProject.value = null
}

const submitContact = async () => {
  loading.value = true
  successMessage.value = ''
  
  try {
    await api.sendContact(contactForm.value)
    successMessage.value = t('contact.success')
    contactForm.value = { nom: '', email: '', telephone: '', type_projet: '', message: '' }
  } catch (error) {
    successMessage.value = t('contact.error')
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

  // Animer le message de chargement toutes les 4 secondes (cold start Render ~30s)
  loadingTimer = setInterval(() => {
    loadingMsgIndex.value++
  }, 4000)

  try {
    const [projectsResponse, techResponse] = await Promise.all([
      api.getProjects(),
      api.getTechnologies()
    ])
    projects.value = parseProjectsResponse(projectsResponse.data)
    technologies.value = techResponse.data.results || techResponse.data
  } catch (error) {
    console.error('Erreur chargement donnees:', error)
    projectsError.value = t('portfolio.error')
  } finally {
    clearInterval(loadingTimer)
    projectsLoading.value = false
  }
}

onMounted(() => {
  if (isDarkMode.value) document.documentElement.classList.add('dark'); else document.documentElement.classList.remove('dark')
  // Charger les projets immédiatement au montage
  loadData()
  trackEvent('home')

  // Initialiser AOS si disponible
  if (typeof AOS !== 'undefined') {
    AOS.init()
  }
})
</script>

<style scoped>
/* Spinner de chargement personnalisé */
.loader-ring {
  width: 56px;
  height: 56px;
  border: 4px solid rgba(16, 185, 129, 0.15);
  border-top-color: #10b981;
  border-radius: 50%;
  animation: spin 0.9s linear infinite;
}

@keyframes spin {
  to { transform: rotate(360deg); }
}

/* Placeholder CSS pour les projets sans image — aucune dépendance externe */
.project-placeholder {
  background: linear-gradient(135deg, #1a2e2a 0%, #0f1f1b 100%);
}

/* Carte projet */
.project-card {
  transition: all 0.3s ease;
}
.project-card:hover {
  transform: translateY(-4px);
  box-shadow: 0 8px 32px rgba(16, 185, 129, 0.12);
}

/* Line-clamp pour la description */
.line-clamp-2 {
  display: -webkit-box;
  -webkit-line-clamp: 2;
  line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
}
</style>
