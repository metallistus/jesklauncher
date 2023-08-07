/* <i class="fa-regular fa-sun"></i> */

const theme = document.querySelector('#theme')
const page__image__mask = document.querySelector('.page__image__mask')

const chill__mode = document.querySelector('.chill__mode')
const chill__mode__exit = document.querySelector('.chill__mode__exit')


if (localStorage.getItem('theme')) {
   show_theme(localStorage.getItem('theme'))
} else {
   show_theme('light')
}

theme.onclick = () => {
   if (page__image__mask.style.backgroundColor === 'rgba(0, 0, 0, 0.6)') {
      show_theme('light')
      localStorage.setItem('theme', 'light')
   } else {
      show_theme('dark')
      localStorage.setItem('theme', 'dark')
   }
}


function show_theme(style) {
   if (style === 'dark') {
      theme.innerHTML = '<i class="fa-regular fa-moon"></i>'
      page__image__mask.style.backgroundColor = 'rgba(0, 0, 0, 0.6)';

      chill__mode.style.backgroundColor = 'rgba(0, 0, 0, 1)'
      chill__mode__exit.style.color = 'white';
   } else {
      theme.innerHTML = '<i class="fa-regular fa-sun"></i> '
      page__image__mask.style.backgroundColor ='rgba(255, 255, 255, 0.3)'

      chill__mode.style.backgroundColor = 'rgba(255, 255, 255, 1)'
      chill__mode__exit.style.color = 'white';
   }
}