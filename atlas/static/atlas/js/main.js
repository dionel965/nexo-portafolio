document.addEventListener("DOMContentLoaded", () => {
  const menuBtn = document.querySelector("[data-menu-btn]");
  const nav = document.querySelector("[data-nav]");

  if (menuBtn && nav) {
    menuBtn.addEventListener("click", () => {
      const expandido = menuBtn.getAttribute("aria-expanded") === "true";
      menuBtn.setAttribute("aria-expanded", String(!expandido));
      nav.classList.toggle("abierto");
    });
  }

  const reflexionBtn = document.querySelector("[data-reflexion-btn]");
  const reflexionTexto = document.querySelector("[data-reflexion-texto]");

  if (reflexionBtn && reflexionTexto) {
    reflexionBtn.addEventListener("click", () => {
      reflexionTexto.classList.toggle("oculto");
    });
  }
});