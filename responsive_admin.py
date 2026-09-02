import re

with open('src/views/Admin.vue', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Main container padding
content = content.replace('p-8 flex flex-col relative', 'p-4 sm:p-8 flex flex-col relative')

# 2. Stats cards grid
content = content.replace('grid-cols-1 md:grid-cols-2 xl:grid-cols-4 gap-4 mb-8', 'grid-cols-2 xl:grid-cols-4 gap-3 sm:gap-4 mb-6 sm:mb-8')

# 3. Stats cards padding & styling
# They all start with bg-gradient-to-br ... rounded-2xl p-6
content = content.replace('rounded-2xl p-6 border', 'rounded-xl sm:rounded-2xl p-3 sm:p-6 border')
content = content.replace('p-3 bg-emerald', 'p-2 sm:p-3 bg-emerald')
content = content.replace('p-3 bg-blue', 'p-2 sm:p-3 bg-blue')
content = content.replace('p-3 bg-purple', 'p-2 sm:p-3 bg-purple')
content = content.replace('p-3 bg-amber', 'p-2 sm:p-3 bg-amber')

# Icons inside stats cards (h-6 w-6 -> h-5 w-5 sm:h-6 sm:w-6)
# Actually it's easier to just do it precisely if there are exactly 4
content = content.replace('h-6 w-6 text-emerald-400', 'h-5 w-5 sm:h-6 sm:w-6 text-emerald-400')
content = content.replace('h-6 w-6 text-blue-400', 'h-5 w-5 sm:h-6 sm:w-6 text-blue-400')
content = content.replace('h-6 w-6 text-purple-400', 'h-5 w-5 sm:h-6 sm:w-6 text-purple-400')
content = content.replace('h-6 w-6 text-amber-400', 'h-5 w-5 sm:h-6 sm:w-6 text-amber-400')

# Text sizes inside stats
content = content.replace('text-3xl font-black text-gray-900', 'text-xl sm:text-3xl font-black text-gray-900')
content = content.replace('text-sm font-medium mb-1', 'text-xs sm:text-sm font-medium mb-1')

# 4. Charts block
content = content.replace('grid-cols-1 lg:grid-cols-2 gap-6 mb-8', 'grid-cols-1 lg:grid-cols-2 gap-4 sm:gap-6 mb-6 sm:mb-8')
content = content.replace('class="h-80"', 'class="h-64 sm:h-80"')
# Reduce padding on chart cards
content = content.replace('rounded-2xl p-6 border border-white/5', 'rounded-xl sm:rounded-2xl p-4 sm:p-6 border border-white/5')

# 5. Quick Actions grid
content = content.replace('grid-cols-1 md:grid-cols-3 gap-4', 'grid-cols-1 sm:grid-cols-3 gap-3 sm:gap-4')
content = content.replace('py-3 rounded-2xl', 'py-2 sm:py-3 rounded-xl sm:rounded-2xl')

# 6. Projects carousel
content = content.replace('flex overflow-x-auto gap-8 pb-10 px-2', 'flex overflow-x-auto gap-4 sm:gap-8 pb-6 sm:pb-10 px-1 sm:px-2')
content = content.replace('w-80 h-[450px]', 'w-[260px] sm:w-80 h-[360px] sm:h-[450px]')
content = content.replace('rounded-[2rem]', 'rounded-2xl sm:rounded-[2rem]')

with open('src/views/Admin.vue', 'w', encoding='utf-8') as f:
    f.write(content)
