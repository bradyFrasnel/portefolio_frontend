import axios from 'axios'

const API_BASE_URL = import.meta.env.VITE_API_URL || 'http://127.0.0.1:8000/api/'

const api = axios.create({
  baseURL: API_BASE_URL,
})

// Intercepteur pour ajouter le token d'authentification
api.interceptors.request.use(config => {
  const token = localStorage.getItem('authToken')
  if (token) {
    // Format DRF : "Token <key>"
    config.headers.Authorization = `Token ${token}`
  }
  return config
}, error => {
  return Promise.reject(error)
})

export default {
  // Authentification Admin
  adminLogin(credentials) {
    return api.post('admin/login/', credentials)
  },

  // Projets
  getProjects(page = 1, search = '') {
    const params = new URLSearchParams({
      page,
      ...(search && { search })
    })
    return api.get(`projects/?${params}`)
  },
  
  getProject(id) {
    return api.get(`projects/${id}/`)
  },

  createProject(data) {
    const fd = new FormData()
    fd.append('project_name', data.project_name)
    fd.append('project_description', data.project_description)
    fd.append('technology_used', data.technology_used)
    if (data.github_link) fd.append('github_link', data.github_link)
    if (data.demo_link) fd.append('demo_link', data.demo_link)
    
    // Si c'est un fichier, on l'ajoute. Si c'est une URL (legacy), on peut aussi l'envoyer.
    if (data.project_image instanceof File) {
      fd.append('project_image', data.project_image)
    } else if (data.project_image) {
      fd.append('project_image', data.project_image)
    }

    return api.post('projects/', fd)
  },

  updateProject(id, data) {
    const fd = new FormData()
    fd.append('project_name', data.project_name)
    fd.append('project_description', data.project_description)
    fd.append('technology_used', data.technology_used)
    if (data.github_link) fd.append('github_link', data.github_link)
    if (data.demo_link) fd.append('demo_link', data.demo_link)
    
    if (data.project_image instanceof File) {
      fd.append('project_image', data.project_image)
    } else if (typeof data.project_image === 'string') {
      // Si on garde l'URL existante lors d'une update
      fd.append('project_image', data.project_image)
    }

    return api.put(`projects/${id}/`, fd)
  },

  deleteProject(id) {
    return api.delete(`projects/${id}/`)
  },
  
  // Technologies  
  getTechnologies() {
    return api.get('technologies/')
  },

  createTechnology(data) {
    return api.post('technologies/', {
      nom: data.nom,
      imageTechnologie: data.imageTechnologie
    })
  },

  updateTechnology(id, data) {
    return api.put(`technologies/${id}/`, {
      nom: data.nom,
      imageTechnologie: data.imageTechnologie
    })
  },

  deleteTechnology(id) {
    return api.delete(`technologies/${id}/`)
  },

  // Contact (si maintenu dans l'API, sinon peut être supprimé s'il n'est plus dans Nouveau.txt)
  sendContact(data) {
    return api.post('contact/', data)
  }
}
