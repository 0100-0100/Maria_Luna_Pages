document.addEventListener("DOMContentLoaded", function () {
  var images = document.querySelectorAll(".carousel-image");
  var swiperInitialized = false;

  function initializeSwiper() {
    if (!swiperInitialized) {
      swiperInitialized = true;
      new Swiper(".swiper-container", {
        slidesPerView: 1,
        centeredSlides: true,
        loop: false,
          navigation: {
          nextEl: ".swiper-button-next",
          prevEl: ".swiper-button-prev",
        },
        pagination: {
          el: ".swiper-pagination",
          clickable: true,
        },
        autoplay: {
          delay: 4000,
          disableOnInteraction: true,
        },
      });
    }
  }

  images.forEach((img) => {
    const imgPreload = new Image();
    const imgUrl = img.dataset.src;

    caches.open("image-cache-v1").then((cache) => {
      cache.match(imgUrl).then((response) => {
        if (response) {
          response.blob().then((blob) => {
            img.src = URL.createObjectURL(blob); // Load from cache
            initializeSwiper();
          });
        } else {
          imgPreload.src = imgUrl;
          imgPreload.onload = () => {
            img.src = imgPreload.src;
            cache.add(imgUrl); // Cache for future use
            initializeSwiper();
          };
        }
      });
    });
  });
});
