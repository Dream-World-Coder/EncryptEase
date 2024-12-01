document.addEventListener("DOMContentLoaded", function () {
  // Select all the anchor tags within the .li elements
  const navLinks = document.querySelectorAll('.nav .li a');

  // Function to handle the intersection observer entries
  const handleIntersect = (entries, observer) => {
      entries.forEach(entry => {
          // Find the corresponding nav link for the intersecting element
          const targetId = entry.target.id;
          const navLink = document.querySelector(`.nav .li a[href="#${targetId}"]`);

          if (entry.isIntersecting) {
              // Add 'active' class to the corresponding li element
              navLink.parentElement.classList.add('active');
          } else {
              // Remove 'active' class from the corresponding li element
              navLink.parentElement.classList.remove('active');
          }
      });
  };

  // Create an intersection observer instance
  const observer = new IntersectionObserver(handleIntersect, {
      root: null, // Use the viewport as the container
      rootMargin: '0px',
      threshold: 0.9 // Trigger when 90% of the element is in the viewport
  });

  // Observe the target sections
  navLinks.forEach(link => {
      const targetId = link.getAttribute('href').substring(1);
      const targetElement = document.getElementById(targetId);

      if (targetElement) {
          observer.observe(targetElement);
      }
  });
});


// phone nav 

const ham = document.getElementById('ham');
const navEl = document.getElementById('n-el');
ham.addEventListener('click', function(){
    navEl.classList.toggle('active');
});