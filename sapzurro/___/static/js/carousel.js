document.addEventListener("DOMContentLoaded", function () {
  var images = document.querySelectorAll(".carousel-image");
  var imagesDescription = document.querySelectorAll(".carousel-description-image");
  images = [...images, ...imagesDescription];
  var swiperInitialized = false;
  var swiperDescriptionInitialized = false;

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

  function initializeSwiperDescription() {
    if (!swiperDescriptionInitialized) {
      swiperDescriptionInitialized = true;
      new Swiper(".swiper-container-description", {
        slidesPerView: 1,
        centeredSlides: true,
        loop: true,
          navigation: {
          nextEl: ".swiper-button-next",
          prevEl: ".swiper-button-prev",
        },
        pagination: {
          el: ".swiper-pagination",
          clickable: true,
        },
        autoplay: {
          delay: 15000,
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
            initializeSwiperDescription();
          });
        } else {
          imgPreload.src = imgUrl;
          imgPreload.onload = () => {
            img.src = imgPreload.src;
            cache.add(imgUrl); // Cache for future use
            initializeSwiper();
            initializeSwiperDescription();
          };
        }
      });
    });
  });
});
