with open('src/views/Admin.vue', 'r', encoding='utf-8') as f:
    content = f.read()

# Fix the main wrapper text color
content = content.replace(
    'class="min-h-screen bg-gray-50 dark:bg-gray-900 text-white p-8 flex flex-col relative"',
    'class="min-h-screen bg-gray-50 dark:bg-gray-900 text-gray-900 dark:text-white p-8 flex flex-col relative"'
)

with open('src/views/Admin.vue', 'w', encoding='utf-8') as f:
    f.write(content)
