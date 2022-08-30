var staticCacheName = "redcrypt_pwa" + new Date().getTime();
var filesToCache = [
    '/offline',
    '/icons/maskable_icon_x192.png',
    '/icons/maskable_icon_x512.png',
    '/offline.svg',
    '/logo_banner.svg',
    '/bg.svg',
    '/scene.glb',
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
                    .filter(cacheName => (cacheName.startsWith("redcrypt-pwa-")))
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
                return caches.match('offline');
            })
    )
});
importScripts('https://cdn.webpushr.com/sw-server.min.js');
