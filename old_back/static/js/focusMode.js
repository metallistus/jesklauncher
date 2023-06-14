const FocusMode = document.querySelector('#FocusMode')

const callender = document.querySelector('.calendar')
const inbox = document.querySelector('.inbox')

const today = document.querySelector('.today')

const page__image__content  = document.querySelector('.page__image__content')


FocusMode.onclick = () => {
   if (callender.style.opacity == '1') {
      page__image__content.style.display = 'flex'
      callender.style.display="none"
      inbox.style.display="none"
      today.style.width = '100%'
      today.style.maxWidth = '800px'
      
      setTimeout(() => {
         inbox.style.opacity = '0'
         callender.style.opacity = '0'
      }, 200)
   } else {
      today.style.width = 'auto'
      page__image__content.style.display = 'grid'
      
      inbox.style.opacity = '1'
      inbox.style.display = "flex"

      callender.style.opacity = '1'
      callender.style.display="flex"
   }
}