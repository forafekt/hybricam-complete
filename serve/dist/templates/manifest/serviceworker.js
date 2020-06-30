// Base Service Worker implementation.  To use your own Service Worker, set the SERVICE_WORKER_PATH variable in settings.py

var staticCacheName = "django-pwa-v" + new Date().getTime();
var filesToCache = [
    '/offline/',
    '/static/css/styles.css',
    '/static/img/icon-72x72.png',
    '/static/img/icon-96x96.png',
    '/static/img/icon-128x128.png',
    '/static/img/icon-144x144.png',
    '/static/img/icon-152x152.png',
    '/static/img/icon-192x192.png',
    '/static/img/icon-384x384.png',
    '/static/img/icon-512x512.png',
    '/static/img/splash-640x1136.png',
    '/static/img/splash-750x1334.png',
    '/static/img/splash-1242x2208.png',
    '/static/img/splash-1125x2436.png',
    '/static/img/splash-828x1792.png',
    '/static/img/splash-1242x2688.png',
    '/static/img/splash-1536x2048.png',
    '/static/img/splash-1668x2224.png',
    '/static/img/splash-1668x2388.png',
    '/static/img/splash-2048x2732.png'
];

// Cache on install
self.addEventListener("install", event => {
    this.skipWaiting();
    event.waitUntil(
        caches.open(staticCacheName)
            .then(cache => {
                return cache.addAll(filesToCache);
            })
    )
});

// Clear cache on activate
self.addEventListener('activate', event => {
    event.waitUntil(
        caches.keys().then(cacheNames => {
            return Promise.all(
                cacheNames
                    .filter(cacheName => (cacheName.startsWith("django-pwa-")))
                    .filter(cacheName => (cacheName !== staticCacheName))
                    .map(cacheName => caches.delete(cacheName))
            );
        })
    );
});

// Serve from Cache
self.addEventListener("fetch", event => {
    event.respondWith(
        caches.match(event.request)
            .then(response => {
                return response || fetch(event.request);
            })
            .catch(() => {
                return caches.match('/offline/');
            })
    )
});
