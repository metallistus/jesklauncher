document.addEventListener('DOMContentLoaded', () => {
    let create_form = document.querySelector('#todo-create-form')
    let todo_list = document.querySelector('#todo-list')

    let add_note_inbox = document.querySelector('add_note_inbox')

    const showTodos = () => {
        fetch('/api/todos')
            .then(response => response.json())
            .then(data => {
                todo_list.innerHTML = ''

                data.forEach(todo => {
                    const div = document.createElement('div')
                    div.classList.add('note')
                    div.innerHTML = `
                        ${todo.message}
                        <a 
                            class="material-symbols-outlined" 
                            style="border: 1px solid rgb(20,20,20,.3)"
                            id = "${todo.id}"
                        >
                            close
                        </a>
                    `
                    todo_list.appendChild(div)
                })

            })
            .catch(err=> {
                console.error('Error: ', err)
            })
    }

    create_form.addEventListener('submit', (e) => {
        e.preventDefault()

        let formData = new FormData(create_form);
        
        fetch('/api/todos', {
            method: 'POST',
            body: formData
        })
            .then(response => response.json())
            .then(data => {
                showTodos()
                add_note_inbox.value = ''
            })
            .catch(error => {
                console.error('Error:', error);
            });
    })

    todo_list.addEventListener('click', (e) => {
        if (e.target.classList.contains('material-symbols-outlined')) {
            let todoItem = e.target.id;
            
            fetch(`/api/todos/${parseInt(todoItem)}`, {
                method: 'DELETE'
            })
                .then(response => {
                    showTodos()
                })
                .catch(err => {
                    console.error('Error: ', err)
                })
        }
    })

    showTodos()
})