function svgPlaceholder(width, height, text, bgColor = '#111827', textColor = '#10b981') {
  const fontSize = Math.max(14, Math.min(width, height) / 10)
  const svg = `<svg xmlns="http://www.w3.org/2000/svg" width="${width}" height="${height}" viewBox="0 0 ${width} ${height}">
    <rect width="100%" height="100%" fill="${bgColor}"/>
    <text x="50%" y="50%" dominant-baseline="middle" text-anchor="middle" fill="${textColor}" font-family="system-ui,sans-serif" font-size="${fontSize}">${text}</text>
  </svg>`
  return `data:image/svg+xml,${encodeURIComponent(svg)}`
}

export const PLACEHOLDERS = {
  card: svgPlaceholder(400, 225, 'Projet'),
  preview: svgPlaceholder(800, 450, 'Aperçu'),
  detail: svgPlaceholder(1200, 600, 'Projet'),
  admin: svgPlaceholder(800, 450, 'Aperçu'),
}

export function projectImageSrc(project, variant = 'card') {
  const url = project?.image_url || project?.project_image
  return url || PLACEHOLDERS[variant] || PLACEHOLDERS.card
}

export function handleImageError(event, variant = 'card') {
  const fallback = PLACEHOLDERS[variant] || PLACEHOLDERS.card
  if (event.target.src !== fallback) {
    event.target.src = fallback
  }
}
