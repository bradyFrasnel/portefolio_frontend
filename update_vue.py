import re

with open('src/views/Home.vue', 'r', encoding='utf-8') as f:
    content = f.read()

# Add telephone in form template
phone_html = '''            <div class="grid grid-cols-1 md:grid-cols-2 gap-6 mt-6">
              <div>
                <label class="block text-sm font-medium text-gray-600 dark:text-gray-custom mb-2">{{ ('contact.phone') }}</label>
                <input
                  v-model="contactForm.telephone"
                  type="tel"
                  class="w-full px-3 sm:px-4 py-2 sm:py-3 bg-white dark:bg-dark-jungle border border-gray-200 dark:border-gray-800 rounded-lg focus:outline-none focus:ring-2 focus:ring-emerald text-gray-900 dark:text-off-white text-sm sm:text-base"
                  :placeholder="('contact.phone_ph')"
                />
              </div>
              <div>
                <label class="block text-sm font-medium text-gray-600 dark:text-gray-custom mb-2">{{ ('contact.budget') }}</label>
                <select
                  v-model="contactForm.budget"
                  class="w-full px-3 sm:px-4 py-2 sm:py-3 bg-white dark:bg-dark-jungle border border-gray-200 dark:border-gray-800 rounded-lg focus:outline-none focus:ring-2 focus:ring-emerald text-gray-900 dark:text-off-white text-sm sm:text-base"
                >
                  <option value="">{{ ('contact.select_ph') }}</option>
                  <option :value="('contact.budget_small')">{{ ('contact.budget_small') }}</option>
                  <option :value="('contact.budget_med')">{{ ('contact.budget_med') }}</option>
                  <option :value="('contact.budget_large')">{{ ('contact.budget_large') }}</option>
                </select>
              </div>
            </div>'''

# We will inject this before the project_type div
content = content.replace('            <div>\n              <label class="block text-sm font-medium text-gray-600 dark:text-gray-custom mb-2">{{ \n(\'contact.project_type\') }}</label>', 
phone_html + '\n            <div>\n              <label class="block text-sm font-medium text-gray-600 dark:text-gray-custom mb-2">{{ \n(\'contact.project_type\') }}</label>')

# Fallback injection if the above split was wrong:
content = content.replace("            <div>\n              <label class=\"block text-sm font-medium text-gray-600 dark:text-gray-custom mb-2\">{{ ('contact.project_type') }}</label>", 
phone_html + "\n            <div class=\"mt-6\">\n              <label class=\"block text-sm font-medium text-gray-600 dark:text-gray-custom mb-2\">{{ ('contact.project_type') }}</label>")


# Update contactForm ref
content = content.replace("nom: '',\n    email: '',\n    type_projet: '',\n    message: ''", "nom: '',\n    email: '',\n    telephone: '',\n    type_projet: '',\n    budget: '',\n    message: ''")
content = content.replace("contactForm.value = { nom: '', email: '', type_projet: '', message: '' }", "contactForm.value = { nom: '', email: '', telephone: '', type_projet: '', budget: '', message: '' }")

with open('src/views/Home.vue', 'w', encoding='utf-8') as f:
    f.write(content)
