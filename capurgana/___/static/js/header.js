function toggleMenu(e) {
  if (e.dataset.open === "true") {
    e.dataset.open = "false";
    e.nextElementSibling.style.display = 'none';
  } else if (e.dataset.open === "false") {
    e.dataset.open = "true";
    e.nextElementSibling.style.display = 'flex';
  }
}
