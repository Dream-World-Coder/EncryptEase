document.addEventListener('DOMContentLoaded', () => {
  const invertButton = document.getElementById('invert-button');
  invertButton.addEventListener('click', toggleDarkMode);
  const isDarkMode = localStorage.getItem('darkMode') === 'true';
  applyDarkMode(isDarkMode);
});


function applyDarkMode(isDarkMode) {
  const root = document.documentElement;
  // const root = document.getElementById('boody'); 

  const sunIcon = document.getElementById("sun-icon");
  const moonIcon = document.getElementById("moon-icon");
  const sections = document.getElementsByTagName('section');
  // const invertButton = document.getElementById('invert-button');

  if (isDarkMode) {
    root.classList.add('invert');
    // [...sections].forEach(section => section.classList.add('invert'));

    sunIcon.style.display = "flex";
    moonIcon.style.display = "none";
    // invertButton.classList.add('active');
  } else {
    root.classList.remove('invert');
    // [...sections].forEach(section => section.classList.remove('invert'));

    sunIcon.style.display = "none";
    moonIcon.style.display = "flex";
    // invertButton.classList.remove('active');
  }
}

function toggleDarkMode() {
  const root = document.documentElement;
  // const root = document.getElementById('boody');

  const sunIcon = document.getElementById("sun-icon");
  const moonIcon = document.getElementById("moon-icon");
  const sections = document.getElementsByTagName('section');
  // const invertButton = document.getElementById('invert-button');

  root.classList.toggle('invert');
  // [...sections].forEach(section => section.classList.toggle('invert'));

  sunIcon.style.display = sunIcon.style.display === "none" ? "flex" : "none";
  moonIcon.style.display = moonIcon.style.display === "none" ? "flex" : "none";
  // invertButton.classList.toggle('active');
  
  const isDarkMode = root.classList.contains('invert'); 
  // const isDarkMode = [...sections].forEach(section => section.classList.contains('invert'));
  localStorage.setItem('darkMode', isDarkMode);
}
