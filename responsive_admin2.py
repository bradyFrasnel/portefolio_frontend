import re

with open('src/views/Admin.vue', 'r', encoding='utf-8') as f:
    content = f.read()

# Make the technology grid a bit more compact on mobile
content = content.replace('grid-cols-2 sm:grid-cols-3 md:grid-cols-4 lg:grid-cols-6 gap-4', 'grid-cols-2 sm:grid-cols-3 md:grid-cols-4 lg:grid-cols-6 gap-3 sm:gap-4')
content = content.replace('bg-gray-100 dark:bg-gray-700/50 rounded-2xl p-4', 'bg-gray-100 dark:bg-gray-700/50 rounded-xl sm:rounded-2xl p-3 sm:p-4')

# Make the section titles smaller on mobile
content = content.replace('text-2xl font-black text-gray-900', 'text-xl sm:text-2xl font-black text-gray-900')

with open('src/views/Admin.vue', 'w', encoding='utf-8') as f:
    f.write(content)
