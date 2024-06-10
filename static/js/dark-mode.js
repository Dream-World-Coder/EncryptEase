document.addEventListener('DOMContentLoaded', () => {
  const invertButton = document.getElementById('invert-button');
  invertButton.addEventListener('click', toggleDarkMode);
  const isDarkMode = localStorage.getItem('darkMode') === 'true';
  applyDarkMode(isDarkMode);
});


function applyDarkMode(isDarkMode) {
  const root = document.documentElement;
  const sunIcon = document.getElementById("sun-icon");
  const moonIcon = document.getElementById("moon-icon");
  
  if (isDarkMode) {
    root.classList.add('invert');
    sunIcon.style.display = "flex";
    moonIcon.style.display = "none";
  } else {
    root.classList.remove('invert');
    sunIcon.style.display = "none";
    moonIcon.style.display = "flex";
  }
}

function toggleDarkMode() {
  const root = document.documentElement;
  const sunIcon = document.getElementById("sun-icon");
  const moonIcon = document.getElementById("moon-icon");

  root.classList.toggle('invert');
  sunIcon.style.display = sunIcon.style.display === "none" ? "flex" : "none";
  moonIcon.style.display = moonIcon.style.display === "none" ? "flex" : "none";
  
  const isDarkMode = root.classList.contains('invert');
  localStorage.setItem('darkMode', isDarkMode);
}












// const sun = document.getElementById("sun-icon");
// const moon = document.getElementById("moon-icon");
// const invertButton = document.getElementById("invert-button");
// const root = document.documentElement;

// moon.addEventListener("click", () => {
//   root.classList.add("invert");
//   moon.style.display = "none" ;
//   sun.style.display = "inline";
// });

// sun.addEventListener("click", () => {
//   root.classList.remove("invert");
//   moon.style.display = "inline";
//   sun.style.display = "none";
// })