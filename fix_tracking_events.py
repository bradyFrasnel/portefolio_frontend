with open('src/views/Home.vue', 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace("trackEvent('page_view')", "trackEvent('home')")
content = content.replace("trackEvent('project_click', project.id)", "trackEvent('project_detail', project.id)")

with open('src/views/Home.vue', 'w', encoding='utf-8') as f:
    f.write(content)
