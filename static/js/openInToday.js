const notification__messages = document.querySelectorAll('.notification__message')

const notification__titles = document.querySelectorAll('.notification__title')
const notification__time = document.querySelectorAll('.notification__message__time')
const notification__text = document.querySelectorAll('.notification__text')

const today__work = document.querySelector('.today__work')


for (let i = 0; i < notification__messages.length; i++) { 
   notification__messages[i].addEventListener('click', () => {
      today__work.innerHTML = `
         <h2>${notification__titles[i].innerHTML}</h2>
         <p>${notification__text[i].innerHTML}</p>
         <p><b>${notification__time[i].innerHTML}</b></p>
      `
   }) 
}