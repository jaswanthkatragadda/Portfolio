// Mobile nav toggle
const navToggle = document.querySelector(".nav-toggle");
const navLinks = document.getElementById("nav-links");

navToggle?.addEventListener("click", () => {
  const isOpen = navLinks.classList.toggle("is-open");
  navToggle.setAttribute("aria-expanded", String(isOpen));
});

navLinks?.querySelectorAll("a").forEach((link) => {
  link.addEventListener("click", () => {
    navLinks.classList.remove("is-open");
    navToggle?.setAttribute("aria-expanded", "false");
  });
});

const themeToggle = document.getElementById("theme-toggle");

function applyTheme(theme) {
  const validTheme = theme === "dark" ? "dark" : "light";

  document.documentElement.dataset.theme = validTheme;
  localStorage.setItem("theme", validTheme);

  if (themeToggle) {
    themeToggle.textContent = validTheme === "dark" ? "☀️" : "🌙";
  }
}

const savedTheme = localStorage.getItem("theme");
applyTheme(savedTheme === "dark" ? "dark" : "light");

themeToggle?.addEventListener("click", () => {
  const currentTheme = document.documentElement.dataset.theme;
  applyTheme(currentTheme === "dark" ? "light" : "dark");
});

const contactForm = document.getElementById("contact-form");
const formStatus = document.getElementById("form-status");

contactForm?.addEventListener("submit", async (event) => {
  event.preventDefault();

  const submitButton = contactForm.querySelector("button[type='submit']");
  const formData = Object.fromEntries(new FormData(contactForm));

  formStatus.textContent = "Sending...";
  submitButton.disabled = true;

  try {
    const response = await fetch("http://127.0.0.1:5000/api/contact", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(formData)
    });

    const result = await response.json();

    if (!response.ok) {
      throw new Error(result.error || "Unable to send your message.");
    }

    formStatus.textContent = result.message;
    contactForm.reset();
  } catch (error) {
    formStatus.textContent =
      error.message || "Unable to connect to the server.";
  } finally {
    submitButton.disabled = false;
  }
    const API_URL = "https://portfolio-t20f.onrender.com";
});
