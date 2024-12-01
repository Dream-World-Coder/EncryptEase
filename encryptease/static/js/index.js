const innerCircle = document.querySelector('.inner_circle');
const outerCircle = document.querySelector('.outer_circle');
const btn = document.getElementById('spin-btn');
function spin(){
  innerCircle.classList.toggle('spin');
  if(innerCircle.classList.contains('spin')){
    btn.innerHTML = "Stop";
  }else{
    btn.innerHTML = "Spin";
  }
};

// if (innerCircle.classList.contains('spin')){
  //   setTimeout(() => {
  //     innerCircle.classList.remove('spin');
  //   }, 800);
  // }




// parallax.js
const main = document.querySelector('.main');

window.addEventListener('scroll', function(){
  var scrolled = window.scrollY;
  var rate = scrolled * 0.17 * (-1);

  main.style.transform = 'translate3d(0,' + rate + 'px, 0)';
});