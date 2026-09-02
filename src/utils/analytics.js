import api from '../services/api.js';

export function getVisitorId() {
  let visitorId = localStorage.getItem('visitor_id');
  const uuidRegex = /^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$/i;
  
  if (!visitorId || !uuidRegex.test(visitorId)) {
    if (typeof crypto !== 'undefined' && crypto.randomUUID) {
      visitorId = crypto.randomUUID();
    } else {
      visitorId = '10000000-1000-4000-8000-100000000000'.replace(/[018]/g, c =>
        (c ^ crypto.getRandomValues(new Uint8Array(1))[0] & 15 >> c / 4).toString(16)
      );
    }
    localStorage.setItem('visitor_id', visitorId);
  }
  return visitorId;
}

function getBrowser() {
  const ua = navigator.userAgent;
  if (ua.includes('Firefox')) return 'Firefox';
  if (ua.includes('Chrome')) return 'Chrome';
  if (ua.includes('Safari')) return 'Safari';
  if (ua.includes('Edge')) return 'Edge';
  return 'Other';
}

function getDeviceType() {
  return /Mobile|Android|iP(ad|hone|od)/.test(navigator.userAgent) ? 'mobile' : 'desktop';
}

export function trackEvent(eventType, projectId = null) {
  const data = {
    visitor_id: getVisitorId(),
    event_type: eventType,
    browser: getBrowser(),
    device_type: getDeviceType()
  };
  if (projectId) {
    data.project = projectId;
  }
  
  // Fire and forget
  api.trackEvent(data).catch(err => console.error('Error tracking event:', err));
}
