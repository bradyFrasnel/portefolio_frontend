import re

with open('src/views/Admin.vue', 'r', encoding='utf-8') as f:
    content = f.read()

replacements = [
    (r'bg-gray-500 text-white', 'bg-gray-500 text-white'), # Dummy to keep syntax
    (r'text-xl font-bold text-white mb-4', 'text-xl font-bold text-gray-900 dark:text-white mb-4'),
    (r'text-3xl font-black text-white', 'text-3xl font-black text-gray-900 dark:text-white'),
    (r'text-2xl font-black text-white', 'text-2xl font-black text-gray-900 dark:text-white'),
    (r'focus:ring-emerald-500 text-white', 'focus:ring-emerald-500 text-gray-900 dark:text-white'),
    (r'focus:ring-blue-500 text-white', 'focus:ring-blue-500 text-gray-900 dark:text-white'),
    (r'cursor-pointer hover:text-white', 'cursor-pointer hover:text-gray-900 dark:hover:text-white'),
    (r'bg-gray-100 dark:bg-gray-700 hover:bg-gray-600 text-white', 'bg-gray-200 dark:bg-gray-700 hover:bg-gray-300 dark:hover:bg-gray-600 text-gray-900 dark:text-white'),
    (r'bg-gray-600 hover:bg-gray-100 dark:bg-gray-700 text-white', 'bg-gray-200 dark:bg-gray-700 hover:bg-gray-300 dark:hover:bg-gray-600 text-gray-900 dark:text-white')
]

for old, new in replacements:
    content = content.replace(old, new)

with open('src/views/Admin.vue', 'w', encoding='utf-8') as f:
    f.write(content)
