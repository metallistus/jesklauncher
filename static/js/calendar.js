// Full Screen
const FullScreen = document.getElementById('FullScreen')

const chill_mode_title = document.querySelector('.chill__phone__intro__title')
const chill_mode_date = document.querySelector('.chill__phone__date')
const chill_mode_time = document.querySelector('.chill__phone__time')

// const NatureSoundsAudio = document.querySelector('#NatureSoundsAudio')


FullScreen.onclick = () => {
   if (document.documentElement.requestFullscreen()) {
      document.exitFullscreen()
   } else{
      document.documentElement.requestFullscreen()
   }
}

// Chill Mode
const open_chill_mode = document.getElementById('ChillMode')
const chill_mode = document.getElementById('chill__mode')
const close_chill_mode = document.querySelector('.close__chill__mode')

if (localStorage.getItem('chillModedisplay')) {
   chill_mode.style.display = localStorage.getItem('chillModedisplay')
}
if (localStorage.getItem('chillModeOpacity')) {
   chill_mode.style.opacity = localStorage.getItem('chillModeOpacity')
}

open_chill_mode.onclick = () => {
   chill_mode.style.display = 'flex';
   localStorage.setItem('chillModedisplay','flex')
   NatureSoundsAudio.play()

   setTimeout(() => {
      chill_mode.style.opacity = '1'
      localStorage.setItem('chillModeOpacity','1')
      chill_mode.style.animation = 'gradient'
   }, 300)
}

close_chill_mode.onclick = () => {
   chill_mode.style.animation = 'kill-gradient'
   
   setTimeout(() => {
      chill_mode.style.opacity = '0'
      localStorage.setItem('chillModeOpacity','0')
      chill_mode.style.display = 'none';
      NatureSoundsAudio.pause()
      localStorage.setItem('chillModedisplay','none')
   }, 1000)
}

// function renderTime () {
//    let date = new Date()
//    let dayOfWeek = date.getDay();

//    let weekdays = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
//    let weekdayName = weekdays[dayOfWeek]
   
//    chill_mode_title.innerHTML = `${weekdayName}`
//    chill_mode_date.innerHTML = `${date.getDate()}.${date.getMonth()}.${date.getFullYear()}`
//    chill_mode_time.innerHTML = `-- ${date.getHours()} : ${date.getMinutes()} : ${date.getSeconds()} --`
   
//    setTimeout(() => {
//       renderTime()
//    }, 1000)
// }
// renderTime()

// setInterval(() => {
//    console.log(date.getSeconds())
//    chill_mode_time.innerHTML = `-- ${date.getHours()} : ${date.getMinutes()} : ${date.getSeconds()} --`
// }, 1000)

// let date = new Date()
// let now_day = date.getDate()

// const callendar__datas = document.querySelector('.callendar__datas')
// const week__names = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']

// function calendar__render() {
//    for (let week__name of week__names) {
//       callendar__datas.innerHTML += `<span class='callendar__week'>${week__name}</span>`
//    }

//    for (let i = 1; i <=31; i ++) {
//       callendar__datas.innerHTML += `
//       <span class='callendar__data ${now_day == i? 'spec': '' }'>${now_day == i? now_day: i }</span>
//       `
//    }
// }

// calendar__render()
// const callendar__data__all = document.querySelectorAll('.callendar__data')

// for (let callendar__data of callendar__data__all) {
//    callendar__data.addEventListener('click', () => {
//       console.log(callendar__data.innerHTML)
//    })
// }

function createCalendar(elem, year, month) {

   let mon = month - 1; // месяцы в JS идут от 0 до 11, а не от 1 до 12
   let d = new Date(year, mon);

   let table = '<table><tr><th>пн</th><th>вт</th><th>ср</th><th>чт</th><th>пт</th><th>сб</th><th>вс</th></tr><tr>';

   // пробелы для первого ряда
   // с понедельника до первого дня месяца
   // * * * 1  2  3  4
   for (let i = 0; i < getDay(d); i++) {
     table += '<td></td>';
   }

   // <td> ячейки календаря с датами
   while (d.getMonth() == mon) {
     table += '<td>' + d.getDate() + '</td>';

     if (getDay(d) % 7 == 6) { // вс, последний день - перевод строки
       table += '</tr><tr>';
     }

     d.setDate(d.getDate() + 1);
   }

   // добить таблицу пустыми ячейками, если нужно
   // 29 30 31 * * * *
   if (getDay(d) != 0) {
     for (let i = getDay(d); i < 7; i++) {
       table += '<td></td>';
     }
   }

   // закрыть таблицу
   table += '</tr></table>';

   elem.innerHTML = table;
 }

 function getDay(date) { // получить номер дня недели, от 0 (пн) до 6 (вс)
   let day = date.getDay();
   if (day == 0) day = 7; // сделать воскресенье (0) последним днем
   return day - 1;
 }

 const callendar__header = document.querySelector('#callendar__header')

 const left = document.createElement('left')
 const right = document.createElement('right')
 const h3 = document.createElement('h3')

 left.innerHTML = '<'
 right.innerHTML = '>'

 const currentDate = new Date()

 let month = currentDate.getMonth()
 let year = currentDate.getFullYear()

 left.onclick = () => {
  //  console.log('left')

   month--

   if (month == 0 ) {
    month = 11
    year--
   } 

   monthRender(h3, month)
   createCalendar(calendar, year, month+1);
 }

 right.onclick = () => {
  //  console.log('right')

   month++

   if (month == 12 ) {
    month = 0
    year++
   } 

   monthRender(h3, month)
   createCalendar(calendar, year, month+1);
 }

 const monthRender = (place, number) => {
   let monthNames = [
      'Январь', 'Февраль', 'Март', 'Апрель',
      'Май', 'Июнь', 'Июль', 'Август',
      'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь'
    ];

   place.innerHTML = `
   ${monthNames[number]} 
   ${year}
   `
 }

 monthRender(h3, month)
 createCalendar(calendar, year, month+1);

callendar__header.append(left, h3, right)

const callendar__place__input = document.querySelector('.callendar__place__input')

callendar__place__input.addEventListener('change', (e) => {
  // console.log(e.target.value)

  year = e.target.value

  monthRender(h3, month)
  createCalendar(calendar, year, month+1);
})