import re

with open('src/views/Home.vue', 'r', encoding='utf-8') as f:
    content = f.read()

# Using regex to remove the budget block
content = re.sub(
    r'<div>\s*<label[^>]*>\{\{\s*\\(\'contact\.budget\'\)\s*\}\}</label>.*?</div>',
    '',
    content,
    flags=re.DOTALL
)

# Fix the grid layout for the phone field
# Before it was: <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
# Which applied to phone and budget. Now it only has phone, so we remove the grid or just leave it (it will take full width or 1 column)
# Let's just change it to a normal div
content = content.replace('<div class="grid grid-cols-1 md:grid-cols-2 gap-6">', '<div>')
# And remove one closing div
# Actually, let's just do an exact surgical replacement.
