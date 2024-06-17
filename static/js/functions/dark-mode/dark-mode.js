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
  // const invertButton = document.getElementById('invert-button');

  if (isDarkMode) {
    root.classList.add('invert');
    sunIcon.style.display = "flex";
    moonIcon.style.display = "none";
    // invertButton.classList.add('active');
  } else {
    root.classList.remove('invert');
    sunIcon.style.display = "none";
    moonIcon.style.display = "flex";
    // invertButton.classList.remove('active');
  }
}

function toggleDarkMode() {
  const root = document.documentElement;
  const sunIcon = document.getElementById("sun-icon");
  const moonIcon = document.getElementById("moon-icon");
  // const invertButton = document.getElementById('invert-button');

  root.classList.toggle('invert');
  sunIcon.style.display = sunIcon.style.display === "none" ? "flex" : "none";
  moonIcon.style.display = moonIcon.style.display === "none" ? "flex" : "none";
  // invertButton.classList.toggle('active');
  
  const isDarkMode = root.classList.contains('invert');
  localStorage.setItem('darkMode', isDarkMode);
}
