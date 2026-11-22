document.addEventListener("DOMContentLoaded", () => {

  // 1. Menú desplegable en móvil
  const menuToggle = document.getElementById("menuToggle");
  const navLinks = document.getElementById("navLinks");

  if (menuToggle && navLinks) {
    menuToggle.addEventListener("click", () => {
      navLinks.classList.toggle("is-open");
    });
  }

  // 2. Filtro de proyectos sin recargar la página
  const filterButtons = document.querySelectorAll(".filter-btn");
  const projectCards = document.querySelectorAll(".project-card");

  if (filterButtons.length && projectCards.length) {
    filterButtons.forEach((btn) => {
      btn.addEventListener("click", () => {
        filterButtons.forEach((b) => b.classList.remove("active"));
        btn.classList.add("active");

        const selected = btn.dataset.filter;

        projectCards.forEach((card) => {
          const tags = (card.dataset.tags || "").split(" ");
          if (selected === "all" || tags.includes(selected)) {
            card.classList.remove("is-hidden");
          } else {
            card.classList.add("is-hidden");
          }
        });
      });
    });
  }

  // 3. Validación del formulario de contacto (sin enviar a ningún servidor)
  const contactForm = document.getElementById("contactForm");
  const formFeedback = document.getElementById("formFeedback");

  if (contactForm && formFeedback) {
    contactForm.addEventListener("submit", (event) => {
      event.preventDefault();

      const nombre = document.getElementById("nombre").value.trim();
      const correo = document.getElementById("correo").value.trim();
      const mensaje = document.getElementById("mensaje").value.trim();
      const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

      formFeedback.className = "form-feedback";

      if (!nombre || !correo || !mensaje) {
        formFeedback.textContent = "Por favor completa todos los campos obligatorios.";
        formFeedback.classList.add("error");
        return;
      }

      if (!emailRegex.test(correo)) {
        formFeedback.textContent = "Ingresa un correo electrónico válido (por ejemplo: nombre@dominio.com).";
        formFeedback.classList.add("error");
        return;
      }

      formFeedback.textContent = `¡Gracias, ${nombre}! Tu mensaje fue validado correctamente.`;
      formFeedback.classList.add("success");
      contactForm.reset();
    });
  }

});