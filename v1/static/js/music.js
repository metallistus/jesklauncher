const music_button = document.querySelector('#NatureSounds')

const NatureSoundsText = document.querySelector('#NatureSoundsText')
const wind = document.querySelector('.callendar__window')

const NatureSoundsAudio = document.querySelector('#NatureSoundsAudio')
const NatureSoundsSelect = document.querySelector('#NatureSoundsSelect')

music_button.onclick = () => {
   if (wind.style.display == 'none') {
      wind.style.display = 'flex';

      setTimeout(() => {
         wind.style.opacity = '1';
      }, 200)

   } else {
      wind.style.opacity = '0';

      setTimeout(() => {
         wind.style.display = 'none';
      }, 200)
   }
}

NatureSoundsSelect.addEventListener('change', (e) => {
   NatureSoundsAudio.src = e.target.value
   NatureSoundsAudio.play()
});

NatureSoundsAudio.addEventListener('ended', function() {
   this.currentTime = 0;
   this.play();
});

const timer__left = document.querySelector('.window__timer__left')
const timer__right = document.querySelector('.window__timer__right')

const runTimer = document.querySelector('#runTimer')
const restartTime = document.querySelector('#restartTime')

const getMinutes = document.querySelector('#getMinutes')
const getSeconds = document.querySelector('#getSeconds')


let minutes = 5
let seconds = 0

// GET MINUTE's
getMinutes.addEventListener('change', (e) => {
   checking(e.target.value, getMinutes)

   timer__left.innerHTML = padZero(e.target.value)
   minutes = e.target.value
})

// GET SECONDS's
getSeconds.addEventListener('change', (e) => {
   num = checking(e.target.value, getSeconds)

   timer__right.innerHTML = padZero(e.target.value)
   seconds = e.target.value
})

timer__left.innerHTML = padZero(minutes)
timer__right.innerHTML = padZero(seconds)

let IntervalId
let timer_status = true

runTimer.addEventListener('click', (e) => {
   if (minutes < 0 || seconds < 0) {
      minutes = seconds = 0
   }
   if (timer_status) {
      IntervalId = setInterval(()=> {
         if (seconds == 0 && minutes == 0) {

            minutes = seconds = 0

            timer__left.innerHTML = padZero(minutes)
            timer__right.innerHTML = padZero(seconds)
            NatureSoundsText.innerHTML = `${padZero(minutes)} : ${padZero(seconds)}`

            clearInterval(IntervalId)
            document.getElementById('chill__mode').style.display = 'flex'
            document.getElementById('chill__mode').style.opacity = 1
            
            NatureSoundsAudio.play()
         }
         if (seconds == 0) {
            seconds = 59
            minutes--
         }
         seconds--
         console.log(minutes, seconds)

         timer__left.innerHTML = padZero(minutes)
         timer__right.innerHTML = padZero(seconds)
         NatureSoundsText.innerHTML = `${padZero(minutes)} : ${padZero(seconds)}`
      },  1000)
      timer_status = false
      runTimer.innerHTML = '<i class="fa-solid fa-pause"></i>'
   } else {
      clearInterval(IntervalId)
      timer_status = true
      runTimer.innerHTML = '<i class="fa-solid fa-play"></i>'
   }
})

restartTime.addEventListener('click', () => {
   clearInterval(IntervalId)
})

// For field check
function checking (value, object ) {
   if (value > 59) {
      object.value = 59
      value = 59
   }
   if (value< 0) {
      object.value = 0
      value = 0
   }

   return value
}

// For Stay Zero's
function padZero(value) {
   return value.toString().padStart(2, '0');
 }
