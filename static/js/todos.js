// Open the inbox and Close
const notes_button = document.querySelector('.inbox__tasks__menu__button')
const notifications = document.querySelector('.column__notifications')
const show_notes= document.querySelector('.inbox__show__tasks')

if (localStorage.getItem('show_notes_notifications')) { 
   notifications.style.height = localStorage.getItem('show_notes_notifications')
}

notes_button.onclick = () => {
   if  (notifications.style.height == '10vh') {
      notifications.style.height = '76vh'
      localStorage.setItem('show_notes_notifications', '76vh')
   } else {
      notifications.style.height = '10vh'
      localStorage.setItem('show_notes_notifications', '10vh')
   }
}

// get and create notes
const place_for_notes = document.querySelector('.inbox__show__tasks')
const notification_number = document.querySelector('.inbox__add__tasks__notification__number');

place_for_notes.innerHTML = ''


// GET notes
const getNotes = async () => {
   let response = await fetch('/api/notes')
   let data = await response.json()

   if (data.count  == '0') {
      renderError(data)
   } else {
      notification_number.innerHTML = data.count
      data.data.map((note) => {
         renderNote(note)
      })
   }
}

getNotes()

function renderNote(note) {
      place_for_notes.innerHTML += `
         <div class='note'>
            ${note.message} 
            <a class='note__delete' href="/tasks/${note.id}/delete"><i class="fa-solid fa-xmark"></i></a>
         </div>
      `
}

function renderError(data) {
   notification_number.innerHTML = data.count
   place_for_notes.innerHTML = `<h4>${data.message}</h4>`
}


const inbox_tasks = document.querySelector('.inbox__tasks');
const add_note = document.querySelector('.add_note');

inbox_tasks.addEventListener('submit',  (e) => {
   e.preventDefault()
   let data = add_note.value

   fetch('/api/notes', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
         message: data
      }), 
    })
      .then(response => response.json())
      .then(data => {
        console.log(data);

        notification_number.innerHTML = parseInt(notification_number.innerHTML)+1
        renderNote(data)
        add_note.value = ''
      })
      .catch(error => {
        console.error(error);
      });
    
})