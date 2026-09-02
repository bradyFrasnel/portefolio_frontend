with open('src/views/Home.vue', 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace(
    "const isDarkMode = ref(true)",
    "const isDarkMode = ref(localStorage.getItem('theme') === 'dark' || (!('theme' in localStorage) && window.matchMedia('(prefers-color-scheme: dark)').matches))"
)

content = content.replace(
    "const toggleDarkMode = () => {\n  isDarkMode.value = !isDarkMode.value\n  document.documentElement.classList.toggle('dark')\n}",
    "const toggleDarkMode = () => {\n  isDarkMode.value = !isDarkMode.value\n  if (isDarkMode.value) {\n    document.documentElement.classList.add('dark')\n    localStorage.setItem('theme', 'dark')\n  } else {\n    document.documentElement.classList.remove('dark')\n    localStorage.setItem('theme', 'light')\n  }\n}"
)

# Also update the initial onMounted to set the theme correctly
content = content.replace(
    "document.documentElement.classList.add('dark')",
    "if (isDarkMode.value) document.documentElement.classList.add('dark'); else document.documentElement.classList.remove('dark')"
)

with open('src/views/Home.vue', 'w', encoding='utf-8') as f:
    f.write(content)
