/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{vue,js,ts,jsx,tsx}",
  ],
  darkMode: 'class',
  theme: {
    extend: {
      colors: {
        'obsidian': '#0a0a0a',
        'dark-jungle': '#121e16',
        'emerald': '#10b981',
        'neon-lime': '#d9f99d',
        'off-white': '#f9f9f9',
        'gray-custom': '#9ca3af',
      },
      fontFamily: {
        'inter': ['Inter', 'sans-serif'],
        'mono': ['JetBrains Mono', 'monospace'],
      },
    },
  },
  plugins: [],
}
