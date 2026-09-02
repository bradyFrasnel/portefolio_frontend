import os
import re

files = [
    'src/views/Home.vue',
    'src/views/Admin.vue',
    'src/components/Footer.vue',
    'src/App.vue'
]

replacements = {
    r'\bbg-obsidian\b': 'bg-gray-50 dark:bg-obsidian',
    r'\bbg-dark-jungle\b': 'bg-white dark:bg-dark-jungle',
    r'\btext-off-white\b': 'text-gray-900 dark:text-off-white',
    r'\btext-gray-custom\b': 'text-gray-600 dark:text-gray-custom',
    r'\bborder-gray-800\b': 'border-gray-200 dark:border-gray-800',
    r'\bbg-gray-800\b': 'bg-gray-200 dark:bg-gray-800',
    r'\btext-gray-300\b': 'text-gray-700 dark:text-gray-300',
    r'\btext-gray-400\b': 'text-gray-500 dark:text-gray-400',
    r'\btext-gray-200\b': 'text-gray-800 dark:text-gray-200',
    r'\bbg-gray-700\b': 'bg-gray-100 dark:bg-gray-700',
    r'\bbg-gray-900\b': 'bg-gray-50 dark:bg-gray-900',
    r'\bborder-gray-700\b': 'border-gray-300 dark:border-gray-700',
    r'\bborder-gray-600\b': 'border-gray-300 dark:border-gray-600',
}

for filepath in files:
    if not os.path.exists(filepath): continue
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    for old, new in replacements.items():
        # Only replace if not already prefixed with dark:
        content = re.sub(r'(?<!dark:)' + old, new, content)
        
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
