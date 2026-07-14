import axios from 'axios'

const API_BASE_URL = import.meta.env.VITE_API_URL || 'https://portefolio-backend-v0e0.onrender.com/api/'

const api = axios.create({
  baseURL: API_BASE_URL,
  timeout: 90000,
  withCredentials: true,
})

api.interceptors.request.use(config => {
  const token = localStorage.getItem('authToken')
  if (token) {
    config.headers.Authorization = `Token ${token}`
  }
  return config
})

async function withRetry(requestFn, retries = 2) {
  let lastError
  for (let attempt = 0; attempt <= retries; attempt++) {
    try {
      return await requestFn()
    } catch (error) {
      lastError = error
      if (attempt < retries) {
        await new Promise(resolve => setTimeout(resolve, 2000 * (attempt + 1)))
      }
    }
  }
  throw lastError
}

export default {
  adminLogin(credentials) {
    return api.post('admin/login/', credentials)
  },

  getProjects(page = 1, search = '') {
    const params = new URLSearchParams({
      page,
      ...(search && { search }),
    })
    return withRetry(() => api.get(`projects/?${params}`))
  },

  getProject(id) {
    return withRetry(() => api.get(`projects/${id}/`))
  },

  createProject(data) {
    const fd = new FormData()
    fd.append('project_name', data.project_name)
    fd.append('project_description', data.project_description)
    fd.append('technology_used', data.technology_used)
    if (data.github_link) fd.append('github_link', data.github_link)
    if (data.demo_link) fd.append('demo_link', data.demo_link)
    if (data.project_image instanceof File) {
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
    }
    return api.put(`projects/${id}/`, fd)
  },

  deleteProject(id) {
    return api.delete(`projects/${id}/`)
  },

  getTechnologies() {
    return withRetry(() => api.get('technologies/'))
  },

  createTechnology(data) {
    return api.post('technologies/', {
      nom: data.nom,
      imageTechnologie: data.imageTechnologie,
    })
  },

  updateTechnology(id, data) {
    return api.put(`technologies/${id}/`, {
      nom: data.nom,
      imageTechnologie: data.imageTechnologie,
    })
  },

  deleteTechnology(id) {
    return api.delete(`technologies/${id}/`)
  },

  sendContact(data) {
    return api.post('contact/', data)
  },
}
