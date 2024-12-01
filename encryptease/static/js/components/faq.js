const openUpIcons = document.querySelectorAll('.upArrow');
const openDownIcons = document.querySelectorAll('.downArrow');
const openCloseBtns = document.querySelectorAll('.open-close');
const questions = document.querySelectorAll('.qn');
const answers = document.querySelectorAll('.ans')


questions.forEach((btn, index) => {
    btn.addEventListener('click', () => {
        const isOpen = answers[index].classList.toggle('open');
        if (isOpen) {
            openUpIcons[index].classList.add('visible');
            openDownIcons[index].classList.add('hidden');
        } else {
            openUpIcons[index].classList.remove('visible');
            openDownIcons[index].classList.remove('hidden');
        }
        answers.forEach((answer, index1) =>{
            if (index1 !== index) {
                answer.classList.remove('open');
                openUpIcons[index1].classList.remove('visible');
                openDownIcons[index1].classList.remove('hidden');
            }
        });
    });
});
