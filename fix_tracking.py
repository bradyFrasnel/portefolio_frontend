import re

with open('src/views/Home.vue', 'r', encoding='utf-8') as f:
    content = f.read()

# Add import
import_stmt = "import { trackEvent } from '../utils/analytics.js'\n"
content = content.replace("import api from '../services/api.js'", import_stmt + "import api from '../services/api.js'")

# Modify showProjectDetail
content = content.replace(
    "const showProjectDetail = (project) => {\n  selectedProject.value = project\n}",
    "const showProjectDetail = (project) => {\n  selectedProject.value = project\n  trackEvent('project_click', project.id)\n}"
)

# Add page_view to onMounted
content = content.replace(
    "loadData()",
    "loadData()\n  trackEvent('page_view')"
)

with open('src/views/Home.vue', 'w', encoding='utf-8') as f:
    f.write(content)
