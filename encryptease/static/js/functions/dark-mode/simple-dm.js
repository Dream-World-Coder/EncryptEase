document.addEventListener('DOMContentLoaded', () => {
  const toggleButton = document.getElementById('invert-button');
  const root = document.documentElement;

  toggleButton.addEventListener('click', () => {
    if (root.classList.contains('dark-mode')) {
      root.classList.remove('dark-mode');
      localStorage.setItem('darkMode', 'false');
    } else {
      root.classList.add('dark-mode');
      localStorage.setItem('darkMode', 'true');
    }
  });

  // Apply dark mode based on localStorage
  const isDarkMode = localStorage.getItem('darkMode') === 'true';
  if (isDarkMode) {
    root.classList.add('dark-mode');
  }
});




// const sun = document.getElementById("sun-icon");
// const moon = document.getElementById("moon-icon");
// const invertButton = document.getElementById("invert-button");
// const root = document.documentElement;

// moon.addEventListener("click", () => {
//   root.classList.add("invert");
//   moon.style.display = "none" ;
//   sun.style.display = "flex";
//   invertButton.classList.add('active');
// });

// sun.addEventListener("click", () => {
//   root.classList.remove("invert");
//   moon.style.display = "flex";
//   sun.style.display = "none";
//   invertButton.classList.remove('active');
// })