document.addEventListener('DOMContentLoaded', () => {
    let messages_list = document.getElementById('messages-list');    

    const showMessages = () => {
        fetch('/api/messages')
            .then((response) => response.json())
            .then((data) => {
                messages_list.innerHTML = ''

                if (data.status == 'success') {
                    data.messages.forEach((message) => {
                        const div = document.createElement('div')
                        div.classList.add('notification')
                        div.id = `${message.id}_notification`
                        div.innerHTML = `
                            <div class="notification__header">
                                <img src="" alt="">
                                <span>${message.type}</span>
                            </div>
                            <div class="notification__body">
                                <div class="notification__message">
                                <span class="notification__title" id='${message.id}_title'>${message.title} </span>
                                <span class="notification__message__time">${message.created_time}</span>
                                </div>
                                <div class="notification__links">
                                <a 
                                    href="${ message.link }" 
                                    target="_blank" 
                                    style="color: rgb(20,20,20,.6); border: 1px solid rgb(20,20,20,.3)"
                                >Show</a>
                                </div>
                                <span class="notification__text" >
                                    <h2>${message.sender}</h2>
                                    <p>${message.text}</p>
                                </span>
                            </div>
                        `
                        messages_list.appendChild(div)
                    })
                } else {
                    messages_list.innerHTML = `<h3>${data.message}</h3>`
                }
            })
            .catch((error) => {
                console.error('Error: ', error);
            })
    }

    messages_list.addEventListener('click', (e) => {
        console.log(e.target)
        if (e.target.classList.contains('notification__title')) {
            const id = e.target.id
            console.log(id)
        }
    })    


    showMessages()
})