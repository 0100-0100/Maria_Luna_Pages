const CACHE_NAME = 'image-carousel-cache-v1';
const IMAGE_CACHE_NAME = 'image-cache-v1';
const STATIC_FILES = [
  '/static/css/swiper/swiper-bundle.min.css',
  '/static/js/swiper/swiper-bundle.min.js',
  '/static/js/carousel.js',
  '/static/js/register-sw.js',
  '/static/images/placeholder.jpg',
];

// Install the Service Worker and Cache Static Assets
self.addEventListener('install', event => {
  event.waitUntil(
    caches.open(CACHE_NAME).then(cache => {
      // console.log('Caching static assets...');
      STATIC_FILES.forEach(file => {
        cache.add(file).catch(_=>console.log(`Could not load ${file} to cache`));
      })
      return;
    })
  );
});

// Activate and Clean Old Caches
self.addEventListener('activate', event => {
  event.waitUntil(
    caches.keys().then(keys => {
      return Promise.all(
        keys.map(key => {
          if (key !== CACHE_NAME && key !== IMAGE_CACHE_NAME) {
            // console.log('Deleting old cache:', key);
            return caches.delete(key);
          }
        })
      );
    })
  );
});

// Intercept Network Requests and Cache Images
self.addEventListener('fetch', event => {
  const requestUrl = new URL(event.request.url);

    // Cache images separately
  if (requestUrl.pathname.startsWith('/media/')) {
    event.respondWith(
      caches.open(IMAGE_CACHE_NAME).then(cache => {
        return cache.match(event.request).then(cachedResponse => {
          return cachedResponse || fetch(event.request, {mode: 'no-cors'}).then(response => {
            cache.put(event.request, response.clone()); // Store in cache
            return response;
          });
        });
      })
    );
    return;
  }

  // Serve static assets from cache
  event.respondWith(
    caches.match(event.request).then(cachedResponse => {
      return cachedResponse || fetch(event.request, {mode: 'no-cors'});
    })
  );
});
